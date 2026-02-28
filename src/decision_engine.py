class DecisionEngine:

    def normalize_weights(self, weights):
        total = sum(weights.values())
        return {k: v/total for k, v in weights.items()}

    def weighted_score(self, options, criteria, weights, scores):
        weights = self.normalize_weights(weights)
        results = {}

        for option in options:
            total = 0
            for c in criteria:
                total += scores[option][c] * weights[c]
            results[option] = round(total, 4)

        return sorted(results.items(), key=lambda x: x[1], reverse=True)