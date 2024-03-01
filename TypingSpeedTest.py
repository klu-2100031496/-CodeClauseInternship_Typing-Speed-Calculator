import time

def calculate_wpm(correct_chars, time_taken):
  """Calculates the typing speed in Words Per Minute (WPM)."""
  words = correct_chars / 5  # Assuming 5 characters per word
  wpm = words / (time_taken / 60)  # Convert time to minutes
  return wpm

def main():
  # Define the text to be typed
  text = "This is a sample text to test your typing speed."

  # Print instructions and start timer
  print("Type the following text and press Enter when finished:")
  print(text)
  start_time = time.time()

  # Get user input
  user_input = input("> ")

  # Stop timer and calculate time taken
  end_time = time.time()
  time_taken = end_time - start_time

  # Calculate accuracy and WPM
  correct_chars = 0
  for i in range(len(text)):
    if text[i] == user_input[i]:
      correct_chars += 1
  accuracy = (correct_chars / len(text)) * 100
  wpm = calculate_wpm(correct_chars, time_taken)

  # Display results
  print("\nResults:")
  print(f"Time taken: {time_taken:.2f} seconds")
  print(f"Accuracy: {accuracy:.2f}%")
  print(f"Typing speed: {wpm:.2f} WPM")

  # Provide feedback based on accuracy and speed
  if accuracy >= 90 and wpm >= 60:
    print("Excellent! You have both high accuracy and speed.")
  elif accuracy >= 80 and wpm >= 40:
    print("Good job! You have decent accuracy and speed.")
  else:
    print("Keep practicing! Aim for higher accuracy and speed.")

if __name__ == "__main__":
  main()
