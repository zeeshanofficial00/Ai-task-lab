# ----- FIZZBUZZ GAME -----
n = int(input("Enter a number: "))

for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
print("🎮 Welcome to FizzBuzz Game!")
print("Rules: Type 'Fizz' for multiples of 3, 'Buzz' for multiples of 5, 'FizzBuzz' for both, or the number itself.")

score = 0
for i in range(1, 16):
    answer = input(f"\n{i}: ").strip()

    # Determine the correct answer
    if i % 3 == 0 and i % 5 == 0:
        correct = "FizzBuzz"
    elif i % 3 == 0:
        correct = "Fizz"
    elif i % 5 == 0:
        correct = "Buzz"
    else:
        correct = str(i)

    if answer.lower() == correct.lower():
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer was: {correct}")

print(f"\n🏁 Game Over! Your Score: {score}/15")

