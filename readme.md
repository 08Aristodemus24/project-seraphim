# This repository contains all generalized code snippets and templates relating to model experimentation, training, evaluation, testing, server-side loading, client-side requests, usage documentation, loaders, evaluators, visualizers, and preprocessor utilities, and the model architectures, figures, and final folder

# requirements:
1. git
2. conda
3. python

# Source code usage
1. assuming git is installed clone repository by running `git clone https://github.com/08Aristodemus24/<repo name>`
2. assuming conda is also installed run `conda create -n <environment name e.g. some-environment-name> python=x.x.x`. Note python version should be `x.x.x` for the to be created conda environment to avoid dependency/package incompatibility.
3. run `conda activate <environment name used>` or `activate <environment name used>`.
4. run `conda list -e` to see list of installed packages. If pip is not yet installed run conda install pip, otherwise skip this step and move to step 5.
5. navigate to directory containing the `requirements.txt` file.
5. run `pip install -r requirements.txt` inside the directory containing the `requirements.txt` file
6. after installing packages/dependencies run `python index.py` while in this directory to run app locally

# App usage:
1. control panel of app will have 3 inputs: prompt, temperature, and sequence length. Prompt can be understood as the starting point in which our model will append certain words during generation for instance if the prompt given is "jordan" then model might generate "jordan is a country in the middle east" and so on. Temperature input can be understood as "how much the do you want the model to generate diverse sequences or words?" e.g. if a diversity of 2 (this is the max value for diversity/temperature by the way) then then the model might potentially generate incomprehensible words (almost made up words) e.g. "jordan djanna sounlava kianpo". And lastly Sequence Length is how long do you want the generated sequence to be in terms of character length for isntance if sequence length is 10 then generated sequence would be "jordan is."

# Articles
1. multiple/ensemble model training: 
* https://www.geeksforgeeks.org/lazy-predict-library-in-python-for-machine-learning/
* https://medium.com/omics-diary/how-to-use-the-lazy-predict-library-to-select-the-best-machine-learning-model-65378bf4568e

2. evaluating ensemble models:

# Pre-built template functions for projects:
~ - done
^ - needs further testing
& - needs further understanding
! - needs further tweaking

Loaders:
* load_corpus
* get_chars
* load_lookup_array
* save_lookup_array
* load_meta_data
* save_meta_data
* construct_embedding_dict
* construct_embedding_matrix
* get_cat_cols ~

Preprocessors:
* map_value_to_index
* remove_contractions
* rem_non_alpha_num
* capitalize
* filter_valid
* partition_corpus
* rem_stop_words
* stem_corpus_words
* lemmatize_corpus_words
* string_list_to_list
* flatten_series_of_lists
* sentences_to_avgs
* normalize_ratings
* normalize_rating_matrix
* normalize_train_cross
* encode_features ~

Visualizers:
* plot_train_cross_features
* analyze
* view_words
* data_split_metric_values
* view_value_frequency ! has no x label
* multi_class_heatmap
* view_metric_values
* view_classified_labels
* view_label_freq ! has no x label
* disp_cat_feat ! has x labels but bars are too compressed especially if n unique is large
* describe_col
* visualize_graph
* plot_evolution ~
* view_clusters_3d ~
* ModelResults ! since there might be a shorter version of code for it from the micro-organism-classifier kaggle code
* plot_all_vars ~
* to implement pairplot for newly encoded featuress

# Prebuilt template components for client-side:
* WE NEED TO IMPLEMENT NOW THESE TEMPLATES FOR OUR MICRO-ORGANISM-CLASSIFIER
* submit button ~
* 100vh section for landing page ~
* text input fields ~
* range input fields ~
* number input fields ~
* file input fields ~
* select fields ~
* textarea fields ~
* create custom themed classes to switch between themes for components
* create two column and one column form
* fix width of data-form-content why does it not expand the width of the parent? ~
* fix image upload field spacing
* fix image upload fields image height
* fix image upload fields upload button