export const words = ["the", "of", "and", "a", "to", "in", "is", "you",
    "that", "it", "he", "was", "for", "on", "are", "as", "with", "his", "they",
    "I", "at", "be", "this", "have", "from", "or", "one", "had", "by", "word",
    "but", "not", "what", "all", "were", "we", "when", "your", "can", "said", "there",
    "use", "an", "each", "which", "she", "do", "how", "their", "if", "will", "up",
    "other", "about", "out", "many", "then", "them", "these", "so", "some", "her", "would",
    "make", "like", "him", "into", "time", "has", "look", "two", "more", "write", "go", "see", "number",
    "no", "way", "could", "people", "my", "than", "first", "water", "been", "call", "who", "oil", "its", "now",
    "find", "long", "down", "day", "did", "get", "come", "made", "may", "part", "over", "new",
    "sound", "take", "only", "little", "work", "know", "place", "year", "live", "me",
    "back", "give", "most", "very", "after", "thing", "our", "just", "name", "good", "sentence",
    "man", "think", "say", "great", "where", "help", "through", "much", "before", "line", "right",
    "too", "mean", "old", "any", "same", "tell", "boy", "follow", "came", "want", "show", "also", "around",
    "form", "three", "small", "set", "put", "end", "does", "another", "well", "large", "must", "big", "even", "such",
    "because", "turn", "here", "why", "ask", "went", "men", "read", "need", "land", "different", "home", "us", "move",
    "try", "kind", "hand", "picture", "again", "change", "off", "play", "spell", "air", "away", "animal",
    "house", "point", "page", "letter", "mother", "answer", "found", "study", "still", "learn", "should", "America",
    "world", "high", "every", "near", "add", "food", "between", "own", "below", "country", "plant", "last",
    "school", "father", "keep", "tree", "never", "start", "city", "earth", "eye", "light", "thought", "head", "under",
    "story", "saw", "left", "don't", "few", "while", "along", "might", "close", "something", "seem", "next",
    "hard", "open", "example", "begin", "life", "always", "those", "both", "paper", "together", "got",
    "group", "often", "run", "important", "until", "children", "side", "feet", "car", "mile", "night", "walk",
    "white", "sea", "began", "grow", "took", "river", "four", "carry", "state", "once", "book", "hear", "stop",
    "without", "second", "later", "miss", "idea", "enough", "eat", "face", "watch", "far", "Indian", "really",
    "almost", "let", "above", "girl", "sometimes", "mountain", "cut", "young", "talk", "soon", "list", "song", "being",
    "leave", "family", "it's"];


export function displayWord() {
    typedWord.value = "";
    wordContainer.textContent = words[Math.floor(Math.random() * words.length)];
};