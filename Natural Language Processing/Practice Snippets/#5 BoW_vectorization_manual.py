import string

# this example text is actually our "training data"
training_data = "Five fantastic fish flew off to find faraway functions. Maybe find another five fantastic fish?"
training_data = training_data.translate(
    str.maketrans("", "", string.punctuation)).lower()

def unique_words(text: str or list):
    unique_words_dict = {}
    index = 0
    for word in text:
        if word not in unique_words_dict:
            unique_words_dict[word] = index
            index += 1

    return unique_words_dict

features_dict = unique_words(training_data.split())

# This is our test data
test_data = """Another five fish find another faraway fish."""
test_data = test_data.translate(
    str.maketrans("", "", string.punctuation)).lower()


print("Training data:" + "\n" + training_data)
print("Features dictionary:")
print(features_dict)
print()
print("Test data:" + "\n" + test_data)

features_dict_vector = len(features_dict) * [0]

for word in test_data.split():
    feature_index = features_dict[word]
    features_dict_vector[feature_index] += 1

print("Features Dictionary Vector:")
print(features_dict_vector)