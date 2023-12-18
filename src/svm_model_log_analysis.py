
import re
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Загрузка логов из файла
log_file_path = "java_logs.txt"
with open(log_file_path, "r") as file:
    logs = file.readlines()

# Разделение логов на тексты и метки
log_samples = [(re.sub(r'\[[^\]]+\]', '', log).strip(), re.search(r'\[([^\]]+)\]', log).group(1)) for log in logs]

# Перемешивание данных
np.random.shuffle(log_samples)

# Проверка, что есть хотя бы один пример лога
if not log_samples:
    raise ValueError("No log samples found.")

# Разделение данных на обучающий и тестовый наборы
texts, labels = zip(*log_samples)
X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42)

# Векторизация текстовых данных
vectorizer = CountVectorizer(token_pattern=r'\b\w+\b')
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Проверка, что после векторизации есть хотя бы один пример
if X_train_vec.shape[0] == 0 or X_test_vec.shape[0] == 0:
    raise ValueError("No training or testing samples found after vectorization.")

# Обучение SVM
svm_classifier = SVC(kernel='linear', C=1.0)
svm_classifier.fit(X_train_vec, y_train)

# Предсказание на тестовом наборе
y_pred = svm_classifier.predict(X_test_vec)

# Оценка качества модели
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Вывод отчета по классификации
print("Classification Report:")
print(classification_report(y_test, y_pred))