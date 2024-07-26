# serand
🔄 All-in-one library to generate cryptographically secure random numbers

## Get started

### Installation

**Note** : Python 3.6 or higher is required.

```bash
# Clone the repository
$ git clone https://github.com/greenmagenta/serand.git

# Change the working directory to serand
$ cd serand

# Install python and python-pip if they are not installed

# Install the library
$ python setup.py install
```

### Usage

```py
# Import the library
from serand import SecureRandom

# Create an instance of SecureRandom
random = SecureRandom()

# Initialize the seed for the random number generator
# This step ensures that the random number generator starts with a unique state
random.seed()

# Generate a random integer within a specific range [10, 100]
value = random.randint(10, 100)
print("Random Integer in Range [10, 100]:", value)
```
















### Unit Tests

```bash
# Run unit tests to check all functions
python -m unittest test_serand.py
```

## Documentation

### Initialization

`SecureRandom()`

    Initializes the SecureRandom instance.

`seed(a=None, version=2)`

    Initializes the random number generator.
    Parameters:
        a (None, int, float, str, bytes, bytearray): Seed value. If None, the current system time or an entropy source is used.
        version (int): Specifies the seeding algorithm version. Default is 2.

`getstate()`

    Returns the internal state of the generator.
    Returns:
        State object capturing the current state of the generator.

`setstate(state)`

    Restores the internal state of the generator.
    Parameters:
        state (Any): State object to restore.

### Random Bytes

`randbytes(n)`

    Generates n cryptographically secure random bytes.
    Parameters:
        n (int): Number of bytes to generate.
    Returns:
        bytes: Random bytes.
```py
# Generate 16 random bytes
print("Random Bytes:", random.randbytes(16))
```
### Random Integers

`randrange(start, stop=None, step=1)`

    Returns a randomly selected element from the range.
    Parameters:
        start (int): Start of the range.
        stop (int, optional): End of the range.
        step (int): Step size.
    Returns:
        int: Random element from the range.
```py
# Generate a random element from range(10)
print("Random Element from range(10):", SecureRandom.randrange(10))

# Generate a random element from range(10, 20, 2)
print("Random Element from range(10, 20, 2):", SecureRandom.randrange(10, 20, 2))
```
`randint(a, b)`

    Returns a random integer N such that a <= N <= b.
    Parameters:
        a (int): Lower bound.
        b (int): Upper bound.
    Returns:
        int: Random integer.
```py
# Generate a random integer within a specific range [10, 100]
print("Random Integer in Range [10, 100]:", random.randint(10, 100))
```
`getrandbits(k)`

    Returns a random integer with k random bits.
    Parameters:
        k (int): Number of random bits.
    Returns:
        int: Random integer.
```py
# Generate a random 32-bit integer
print("Random Integer:", random.getrandbits(32))
```

### Random Sequences

`choice(seq)`

    Returns a random element from the non-empty sequence seq.
    Parameters:
        seq (Sequence): Non-empty sequence to choose from.
    Returns:
        Random element from the sequence.
    Raises:
        IndexError: If the sequence is empty.
```py
# Choose a random element from a list
print("Random Choice from [1, 2, 3, 4, 5]:", random.choice([1, 2, 3, 4, 5]))
```
`choices(population, weights=None, cum_weights=None, k=1)`

    Returns a list of size k of elements chosen from the population with replacement.
    Parameters:
        population (Sequence): Population to choose from.
        weights (Sequence of float, optional): Weights for the population elements.
        cum_weights (Sequence of float, optional): Cumulative weights for the population elements.
        k (int): Number of elements to choose.
    Returns:
        List of chosen elements.
    Raises:
        TypeError: If both weights and cum_weights are specified.
```py
# Choose 3 elements from a list with weights
print("Choices from ['a', 'b', 'c'] with weights [0.1, 0.3, 0.6]:", SecureRandom.choices(['a', 'b', 'c'], weights=[0.1, 0.3, 0.6], k=3))
```
`shuffle(x)`

    Shuffles the sequence x in place.
    Parameters:
        x (List): List to shuffle.
```py
# Shuffle a list in place
sample_list = [1, 2, 3, 4, 5]
random.shuffle(sample_list)
print("Shuffled List:", sample_list)
```
`sample(population, k, counts=None)`

    Returns a list of size k of unique elements chosen from the population.
    Parameters:
        population (Sequence): Population to choose from.
        k (int): Number of elements to choose.
        counts (Sequence of int, optional): Counts for the elements in the population.
    Returns:
        List of unique elements.
    Raises:
        ValueError: If sample size k is larger than the population size.
```py
# Generate a random sample of 3 unique elements from a list
print("Sample from [1, 2, 3, 4, 5]:", random.sample([1, 2, 3, 4, 5], 3))
```

### Distributions for Real Numbers

`random()`

    Returns a random floating-point number in the range [0.0, 1.0).
    Returns:
        float: Random floating-point number.
```py
# Generate a random floating-point number in the range [0.0, 1.0)
print("Random Float:", random.random())
```
`uniform(a, b)`

    Returns a random floating-point number N such that a <= N <= b.
    Parameters:
        a (float): Lower bound.
        b (float): Upper bound.
    Returns:
        float: Random floating-point number.
```py
# Generate a random floating-point number in the range [0, 10]
print("Uniform [0, 10]:", random.uniform(0, 10))
```
`triangular(low, high, mode)`

    Returns a random floating-point number N such that low <= N <= high with the specified mode between those bounds.
    Parameters:
        low (float): Lower limit.
        high (float): Upper limit.
        mode (float): Mode of the distribution.
    Returns:
        float: Random floating-point number.
```py
# Generate a random number with a triangular distribution
print("Triangular [0, 10, 5]:", random.triangular(0, 10, 5))
```
`betavariate(alpha, beta)`

    Beta distribution. Returns a random number between 0 and 1.
    Parameters:
        alpha (float): Alpha parameter.
        beta (float): Beta parameter.
    Returns:
        float: Random number.
```py
# Generate a random number with a beta distribution
print("Beta variate [2, 5]:", random.betavariate(2, 5))
```
`expovariate(lambd)`

    Exponential distribution. Returns a random number.
    Parameters:
        lambd (float): 1.0 divided by the desired mean.
    Returns:
        float: Random number.
```py
# Generate a random number with an exponential distribution
print("Exponential variate [1.5]:", random.expovariate(1.5))
```
`gammavariate(alpha, beta)`

    Gamma distribution. Returns a random number.
    Parameters:
        alpha (float): Shape parameter.
        beta (float): Scale parameter.
    Returns:
        float: Random number.
```py
# Generate a random number with a gamma distribution
print("Gamma variate [2, 3]:", random.gammavariate(2, 3))
```
`gauss(mu, sigma)`

    Gaussian distribution. Returns a random number.
    Parameters:
        mu (float): Mean.
        sigma (float): Standard deviation.
    Returns:
        float: Random number.
```py
# Generate a random number with a Gaussian (normal) distribution
print("Gaussian [0, 1]:", random.gauss(0, 1))
```
`lognormvariate(mu, sigma)`

    Log-normal distribution. Returns a random number.
    Parameters:
        mu (float): Mean of the underlying normal distribution.
        sigma (float): Standard deviation of the underlying normal distribution.
    Returns:
        float: Random number.
```py
# Generate a random number with a log-normal distribution
print("Log normal [0, 1]:", random.lognormvariate(0, 1))
```
`normalvariate(mu, sigma)`

    Normal distribution. Returns a random number.
    Parameters:
        mu (float): Mean.
        sigma (float): Standard deviation.
    Returns:
        float: Random number.
```py
# Generate a random number with a normal distribution
print("Normal variate [0, 1]:", random.normalvariate(0, 1))
```
`vonmisesvariate(mu, kappa)`

    Von Mises distribution. Returns a random number.
    Parameters:
        mu (float): Mean angle in radians.
        kappa (float): Concentration parameter.
    Returns:
        float: Random number.
```py
# Generate a random number with a von Mises distribution
print("Von Mises [0, 4]:", random.vonmisesvariate(0, 4))
```
`paretovariate(alpha)`

    Pareto distribution. Returns a random number.
    Parameters:
        alpha (float): Shape parameter.
    Returns:
        float: Random number.
```py
# Generate a random number with a Pareto distribution
print("Pareto [2]:", random.paretovariate(2))
```
`weibullvariate(alpha, beta)`

    Weibull distribution. Returns a random number.
    Parameters:
        alpha (float): Scale parameter.
        beta (float): Shape parameter.
    Returns:
        float: Random number.
```py
# Generate a random number with a Weibull distribution
print("Weibull [1, 1.5]:", random.weibullvariate(1, 1.5))
```
`binomialvariate(n, p)`

    Binomial distribution. Returns a random integer.
    Parameters:
        n (int): Number of trials.
        p (float): Probability of success for each trial.
    Returns:
        int: Number of successes in n trials.
```py
# Generate a random number with a binomial distribution
print("Binomial variate [10, 0.5]:", SecureRandom.binomialvariate(10, 0.5))
```

## Disclamer

This library, `serand`, is experimental and has been developed as an educational tool to demonstrate cryptographically secure random number generation techniques. While it uses the secrets module and system entropy sources to enhance security, it is important to note that the library has not undergone extensive security audits or formal verification.

If you intend to use `serand` in sensitive or critical applications, we strongly recommend conducting a thorough security review and validation to ensure it meets your specific security requirements. Users should exercise caution and perform their own due diligence before relying on this library for any sensitive use cases.

## License

[GPL-3.0](https://github.com/greenmagenta/secure_random/LICENSE/) License
