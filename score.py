class BowlingScore:
    def __init__(self, frames):
        self.frames = frames

    @staticmethod
    def _is_strike(frame_scores):
        return frame_scores[0] == 10

    @staticmethod
    def _is_spare(frame_scores):
        return sum(frame_scores[0:2]) == 10

    def total_score(self):
        total = 0
        for round_index, frame_scores in enumerate(self.frames):
            if self._is_strike(frame_scores) and round_index <= 6:
                total += frame_scores[0]
                total += sum(self.frames[round_index+1])
                if len(self.frames[round_index+1]) == 1:
                    total += self.frames[round_index+2][0]
            elif self._is_strike(frame_scores) and round_index == 7:
                total += frame_scores[0]
                total += sum(self.frames[round_index+1])
                if len(self.frames[round_index + 1]) == 1:
                    total += self.frames[round_index+1][0]
            elif self._is_strike(frame_scores) and round_index == 8:
                total += frame_scores[0]
                total += self.frames[round_index+1][0] + self.frames[round_index+1][1]
            elif self._is_strike(frame_scores) and round_index == 9:
                total += sum(frame_scores)

            elif self._is_spare(frame_scores) and round_index <= 8:
                total += sum(frame_scores)
                total += self.frames[round_index+1][0]

            else:
                total += sum(frame_scores)

        return total
