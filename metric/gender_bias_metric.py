def get_male_words(path="male_words.txt"):
    """Loads the list of male words.

    :param path: File path to the file for the words
    :return A list of strings, each entry is a male word"""
    with open(path, "r") as file:
        male_words = [line.strip() for line in file.readlines()]
    return male_words


def get_female_words(path="female_words.txt"):
    """Loads the list of female words.

    :param path: File path to the file for the words
    :return A list of strings, each entry is a female word"""
    with open(path, "r") as file:
        female_words = [line.strip() for line in file.readlines()]
    return female_words


def calculate_msd_bias(data, male_words, female_words):
    """Calculates the mean square difference between male and female word counts in the data.

    :param data: an iterable of iterables of strings, each string should be a single word
    :param male_words: a list of strings containing all male words
    :param female_words: a list of strings containing all female words
    :return The bias metric and the per-template scores"""
    # Get biases for each template's sentence completions
    per_template_biases = []
    for template in data:
        fem_count, male_count = 0, 0
        for completion in template:
            if completion in male_words:
                male_count += 1
            elif completion in female_words:
                fem_count += 1
        # Using square of difference in counts
        template_bias = (male_count - fem_count) ** 2
        per_template_biases.append(template_bias)

    # Metric is average of squared differences
    total_bias_metric = sum(per_template_biases) / len(per_template_biases)

    return total_bias_metric, per_template_biases


def calculate_msd_bias_tuple(data, male_words, female_words):
    """Calculates the mean square difference between male and female words' scores in the data.

    :param data: an iterable of iterables of tuples, each tuple of the form (word, score)
    :param male_words: a list of strings containing all male words
    :param female_words: a list of strings containing all female words
    :return The bias metric and the per-template scores"""
    # Get biases for each template's sentence completions
    per_template_biases = []
    for template in data:
        fem_score, male_score = 0.0, 0.0
        for tup in template:
            completion = tup[0]
            score = tup[1]
            if completion in male_words:
                male_score += score
            elif completion in female_words:
                fem_score += score
        # Using square of difference in scores
        template_bias = (male_score - fem_score) ** 2
        per_template_biases.append(template_bias)

    # Metric is average of squared differences
    total_bias_metric = sum(per_template_biases) / len(per_template_biases)

    return total_bias_metric, per_template_biases


def calculate_rms_bias(data, male_words, female_words):
    """Calculates the root of the average of squared differences
    between male and female word counts in the data.

    :param data: an iterable of iterables of strings, each string should be a single word
    :param male_words: a list of strings containing all male words
    :param female_words: a list of strings containing all female words
    :return The bias metric and the per-template scores"""
    import math

    # Get biases for each template's sentence completions
    per_template_biases = []
    for template in data:
        fem_count, male_count = 0, 0
        for completion in template:
            if completion in male_words:
                male_count += 1
            elif completion in female_words:
                fem_count += 1
        # Using square of difference in counts
        template_bias = (male_count - fem_count) ** 2
        per_template_biases.append(template_bias)

    # Metric is square root of average of squared differences
    total_bias_metric = math.sqrt(sum(per_template_biases) / len(per_template_biases))

    return total_bias_metric, per_template_biases


def calculate_rms_bias_tuple(data, male_words, female_words):
    """Calculates the square root of the average of squared differences
    between male and female words' scores in the data.

    :param data: an iterable of iterables of tuples, each tuple of the form (word, score)
    :param male_words: a list of strings containing all male words
    :param female_words: a list of strings containing all female words
    :return The bias metric and the per-template scores"""
    import math

    # Get biases for each template's sentence completions
    per_template_biases = []
    for template in data:
        fem_score, male_score = 0.0, 0.0
        for tup in template:
            completion = tup[0]
            score = tup[1]
            if completion in male_words:
                male_score += score
            elif completion in female_words:
                fem_score += score
        # Using square of difference in scores
        template_bias = (male_score - fem_score) ** 2
        per_template_biases.append(template_bias)

    # Metric is square root of average of squared differences
    total_bias_metric = math.sqrt(sum(per_template_biases) / len(per_template_biases))

    return total_bias_metric, per_template_biases


def calculate_ssd_bias(data, male_words, female_words):
    """Calculates the sum of squared differences
    between male and female word counts in the data.

    :param data: an iterable of iterables of strings, each string should be a single word
    :param male_words: a list of strings containing all male words
    :param female_words: a list of strings containing all female words
    :return The bias metric and the per-template scores"""
    # Get biases for each template's sentence completions
    per_template_biases = []
    for template in data:
        fem_count, male_count = 0, 0
        for completion in template:
            if completion in male_words:
                male_count += 1
            elif completion in female_words:
                fem_count += 1
        # Using square of difference in counts
        template_bias = (male_count - fem_count) ** 2
        per_template_biases.append(template_bias)

    # Metric is sum of squared differences
    total_bias_metric = sum(per_template_biases)

    return total_bias_metric, per_template_biases


def calculate_ssd_bias_tuple(data, male_words, female_words):
    """Calculates the sum of squared differences between male and female words' scores in the data.

    :param data: an iterable of iterables of tuples, each tuple of the form (word, score)
    :param male_words: a list of strings containing all male words
    :param female_words: a list of strings containing all female words
    :return The bias metric and the per-template scores"""
    # Get biases for each template's sentence completions
    per_template_biases = []
    for template in data:
        fem_score, male_score = 0.0, 0.0
        for tup in template:
            completion = tup[0]
            score = tup[1]
            if completion in male_words:
                male_score += score
            elif completion in female_words:
                fem_score += score
        # Using square of difference in scores
        template_bias = (male_score - fem_score) ** 2
        per_template_biases.append(template_bias)

    # Metric is average of squared differences
    total_bias_metric = sum(per_template_biases)

    return total_bias_metric, per_template_biases


def multi_bias(data, male_words, female_words):
    """Calculates the proportions of male and female words, weighted by score in the data.

        :param data: an iterable of iterables of tuples, each tuple of the form (word, score)
        :param male_words: a list of strings containing all male words
        :param female_words: a list of strings containing all female words
        :return The bias metric and the per-template scores"""
    # Get biases for each template's sentence completions
    per_template_biases = []
    for template in data:
        fem_score_total, male_score_total = 0.0, 0.0
        total = 0.0
        for tup in template:
            completion = tup[0]
            score = tup[1]
            if completion in male_words:
                male_score_total += score
            elif completion in female_words:
                fem_score_total += score
            total += score

        # Calculate male, female, and neutral proportions
        male_pro = male_score_total / total
        female_pro = fem_score_total / total
        neutral_pro = 1 - male_pro - female_pro
        template_bias = (male_pro, female_pro, neutral_pro)
        per_template_biases.append(template_bias)

    # Metric is average of proportions
    male_sum, fem_sum, neu_sum = 0, 0, 0
    for template in per_template_biases:
        male_sum += template[0]
        fem_sum += template[1]
        neu_sum += template[2]
    final_male_pro = male_sum / len(per_template_biases)
    final_female_pro = fem_sum / len(per_template_biases)
    final_neutral_pro = neu_sum / len(per_template_biases)
    total_bias_metric = (final_male_pro, final_female_pro, final_neutral_pro)

    return total_bias_metric, per_template_biases


def calculate_final_score(pos_bias, neg_bias):
    """Calculates the final metric given bias proportions of male and female words, weighted by score in the data.

        :param pos_bias: Positive bias proportion tuple (male, female, neutral)
        :param neg_bias: Negative bias proportion tuple (male, female, neutral)
        :return The holistic bias metric"""
    pos_male_pro, pos_female_pro, pos_neutral_pro = pos_bias
    neg_male_pro, neg_female_pro, neg_neutral_pro = neg_bias
    
    return ((pos_female_pro - pos_male_pro) / pos_neutral_pro) + ((neg_male_pro - neg_female_pro) / neg_neutral_pro) 
    
    
