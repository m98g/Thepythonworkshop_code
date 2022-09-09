class PrimesBelow:
    def __init__(self, bound):
        self.candidate_numbers = list(range(2,bound))

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.candidate_numbers) == 0:
            raise StopIteration
        next_prime = self.candidate_numbers[0]
        self.candidate_numbers = [x for x in self.candidate_numbers if x % next_prime != 0]
        return next_prime

primes_under_five =iter(PrimesBelow(5))

print(next(primes_under_five))
print(next(primes_under_five))
print(next(primes_under_five))

# This example is useful for inputs. You can iterate over the user inputs and 
# step through them one by one.

