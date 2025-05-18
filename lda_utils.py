import numpy as np
from joblib import Parallel, delayed
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_auc_score
from tqdm import tqdm


# Function to process a single time point (t)
def process_window(
    t,
    window,
    train_A,
    train_B,
    test_A,
    test_B,
    classifier,
):
    # (t, window,num_iter, avg, A, B, n_sensors, super_sample,
    # n_trials, split_idx,sampling_ratio,classifier) = args
    win = []

    # Setup window size
    t2 = min(t + window, train_A.shape[2])

    trial_length = t2 - t
    win = np.arange(t, t2)  # adjust for pythons 0 NOT SURE IF IT WORKS

    # concatenate them
    train_x = np.concatenate((train_A[:, :, win], train_B[:, :, win]), axis=0)
    test_x = np.concatenate((test_A[:, :, win], test_B[:, :, win]), axis=0)
    train_y = np.array([1] * train_A.shape[0] + [2] * train_B.shape[0])
    test_y = np.array([1] * test_A.shape[0] + [2] * test_B.shape[0])

    max_size_train = max(
        train_A.shape[0], train_B.shape[0]
    )  # get the minimum size of data, ideally not
    max_size_test = max(
        test_A.shape[0], test_B.shape[0]
    )  # get the minimum size of data, ideally not

    # print("Calculating Averages")

    train_x, train_y = average_trials(
        train_x, train_y, average_trials=10, max_sampling=max_size_train
    )
    test_x, test_y = average_trials(
        test_x, test_y, average_trials=10, max_sampling=max_size_test
    )

    if np.ndim(train_x) > 2:
        train_x = train_x.reshape(
            train_x.shape[0], train_x.shape[1] * train_x.shape[2]
        )
    if np.ndim(test_x) > 2:
        test_x = test_x.reshape(
            test_x.shape[0], test_x.shape[1] * test_x.shape[2]
        )
    if np.ndim(train_y) > 2:
        train_y = train_y.reshape(
            train_y.shape[0], train_y.shape[1] * train_y.shape[2]
        )
    if np.ndim(test_y) > 2:
        test_y = test_y.reshape(
            test_y.shape[0], test_y.shape[1] * test_y.shape[2]
        )

    if np.any(np.abs(train_x)) != 0:
        classifier.fit(train_x, train_y)

        # test it on same time points
        pred_y = classifier.predict(test_x)
        acc = roc_auc_score(test_y, pred_y)
        return {"AUC": acc, "time": t}
    else:
        return {"AUC": 0, "time": t}


def run_LDA(
    train_A,
    train_B,
    test_A,
    test_B,
    classifier,
    window=1,
    step=1,
):

    all_results = []

    # Add progress bar to joblib.Parallel
    all_results = Parallel(n_jobs=-1)(
        delayed(process_window)(
            t,
            window,
            train_A,
            train_B,
            test_A,
            test_B,
            classifier,
        )
        for t in tqdm(range(0, train_A.shape[2] - window - 1, step))
    )

    return all_results


def prep_decoding_data_hierarchical(
    merged_train,
    merged_test,
    cat_a_spec,
    cat_b_spec,
    train_df,
    test_df,
    category_hierarchy,
    word_column="category_name",
):
    """
    Prepares epoched data for decoding based on potentially hierarchical categories.

    Args:
        epoched_data: The MNE Epochs object containing all data.
        cat_a_spec: A string or list of strings specifying top-level categories
                    (keys in category_hierarchy) or specific words for category A.
        cat_b_spec: A string or list of strings specifying top-level categories
                    (keys in category_hierarchy) or specific words for category B.
        stim_df: Pandas DataFrame with stimulus information. Must include
                 a column with the name specified in `word_column`.
        category_hierarchy: A potentially nested dictionary where keys are category
                            names and values are lists/sets of words or further
                            nested dictionaries of subcategories.
        word_column (str): The name of the column in stim_df containing the
                           individual stimulus words to match against the hierarchy.
                           Defaults to 'word'.

    Returns:
        tuple: (data_a, data_b) containing the selected MNE Epochs objects
               for category A and category B, or empty Epochs selections if no
               data is found for a category.
    """

    # --- Get Words for Each Category Specification ---
    words_a = get_words_in_categories(cat_a_spec, category_hierarchy)
    words_b = get_words_in_categories(cat_b_spec, category_hierarchy)

    print(
        f"Category A Specification '{cat_a_spec}' maps to"
        f" {len(words_a)} words."
    )
    if words_a:
        print(f"  First few A words: {words_a[:10]}...")
    print(
        f"Category B Specification '{cat_b_spec}' maps to"
        f" {len(words_b)} words."
    )
    if words_b:
        print(f"  First few B words: {words_b[:10]}...")

    # --- Filter stim_df to Find Matching Trials ---
    # Use .copy() to avoid SettingWithCopyWarning if stim_df is modified later outside the function
    train_df_a = train_df[train_df[word_column].isin(words_a)]
    train_df_b = train_df[train_df[word_column].isin(words_b)]
    test_df_a = test_df[test_df[word_column].isin(words_a)]
    test_df_b = test_df[test_df[word_column].isin(words_b)]

    # --- Extract Data Using Original Epoch Indices ---
    train_indices_a = train_df_a.index
    train_indices_b = train_df_b.index
    test_indices_a = test_df_a.index
    test_indices_b = test_df_b.index

    print(
        f"Found {len(train_indices_a)} train epochs matching Category A spec."
    )
    if len(train_indices_a):
        print(f"  First few A indices: {train_indices_a[:10]}...")
    else:
        print(
            "Warning: No train epochs found matching Category A specification."
        )
    print(
        f"Found {len(train_indices_b)} train epochs matching Category B spec."
    )
    if len(train_indices_b):
        print(f"  First few B indices: {train_indices_b[:10]}...")
    else:
        print(
            "Warning: No train epochs found matching Category B specification."
        )
    print(f"Found {len(test_indices_a)} test epochs matching Category A spec.")
    if len(test_indices_a):
        print(f"  First few A indices: {test_indices_a[:10]}...")
    else:
        print(
            "Warning: No test epochs found matching Category A specification."
        )
    print(f"Found {len(test_indices_b)} test epochs matching Category B spec.")
    if len(test_indices_b):
        print(f"  First few B indices: {test_indices_b[:10]}...")
    else:
        print(
            "Warning: No test epochs found matching Category B specification."
        )

    return (
        merged_train[train_indices_a],
        merged_train[train_indices_b],
        merged_test[test_indices_a],
        merged_test[test_indices_b],
    )


def get_words_in_categories(categories_spec, hierarchy):
    """
    Collects all unique words associated with the given category names or specific words,
    searching recursively/iteratively through the nested hierarchy starting from the specified items.

    Args:
        categories_spec (list): A list of strings, where each string is either a
                                top-level category key from the hierarchy or a
                                specific word to include directly.
        hierarchy (dict): The potentially nested dictionary defining categories.
                          Values can be lists/sets of words or nested dictionaries.

    Returns:
        list: A list of unique words found under the specified categories or
              included directly from the spec.
    """
    final_words = set()
    items_to_process = list(categories_spec)  # Start with user-provided spec

    while items_to_process:
        item = items_to_process.pop(0)

        if not isinstance(item, str):
            print(
                f"Warning: Skipping non-string item in categories_spec: {item}"
            )
            continue

        # Check if the item is a key in the *top level* of the hierarchy
        if item in hierarchy:
            # It's a category key, start traversal from its value
            value_queue = [
                hierarchy[item]
            ]  # Queue for values within this category branch

            while value_queue:
                current_val = value_queue.pop(0)

                if isinstance(current_val, dict):
                    # If it's a sub-dictionary, add its values to the queue for processing
                    for sub_val in current_val.values():
                        value_queue.append(sub_val)
                elif isinstance(current_val, (list, set, tuple)):
                    # If it's a list/set, assume it contains words
                    final_words.update(
                        w for w in current_val if isinstance(w, str)
                    )
                elif isinstance(current_val, str):
                    # If a string is found directly as a value (less common structure)
                    final_words.add(current_val)
                # Ignore other data types found within the hierarchy values

        else:
            # Item is not a top-level category key, assume it's a specific word
            final_words.add(item)

    return list(final_words)


def average_trials(data, labels, average_trials=5, max_sampling=1000):

    if average_trials < 2:
        averaged_data = data
        averaged_labels = labels
    else:

        averaged_data = []
        averaged_labels = []

        # Separate data based on labels
        unique_labels = np.unique(labels)
        # PARALELLIZE
        for label in unique_labels:
            label_data = data[labels == label]

            # Loop over the data and collect averages with substitution
            for _ in range(int(max_sampling)):
                # Sample with replacement
                indices = np.random.choice(
                    label_data.shape[0], 5, replace=True
                )
                batch_data = label_data[indices]

                # Compute average and append to list
                averaged_trial = np.mean(batch_data, axis=0)
                averaged_data.append(averaged_trial)
                averaged_labels.append(label)

    return np.array(averaged_data), np.array(averaged_labels)
