import tf_glove
model = tf_glove.GloVeModel(embedding_size=50, context_size=10, min_occurrences=25, learning_rate=0.05, batch_size=512)



