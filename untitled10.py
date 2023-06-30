import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
import nltk
from nltk.corpus import stopwords

#Reads the UN declaration file 
file_path = "C:\\Users\\Bhavesh\\Downloads\\un_declaration_hr_text_data.txt"
with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()

#processes the text file 
UNwords = nltk.word_tokenize(content.lower())
stopWords = set(stopwords.words("english"))
EditedWords = [word for word in UNwords if word.isalpha() and word not in stopWords]

# Word frequencies
wordFrequency = Counter(EditedWords)

# Word cloud
wordcloud = WordCloud(
    width=800, height=400, background_color="white", relative_scaling=0.5
)
wordcloud.generate(
    " ".join(EditedWords)
)  # Generate word cloud from the preprocessed text

# Display the Word Cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.savefig("wordcloud.png")

 #Modifies the colours and style for the bar graph
commonWords = wordFrequency.commonWords(25)
words = [word[0] for word in commonWords]
frequency = [word[1] for word in commonWords]

#Makes a bar plot and changes the style
colours = ["#4387f5", "#42f6c5", "#f5cd42", "#f54297", "#9a41f5"]  # Example color palette
plt.figure(figsize=(12, 6))
plt.bar(words, frequency, color=colours)  # Set custom colors
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.xticks(rotation=90)
plt.tight_layout()

# Saves as 
plt.savefig("bargraph.png")
