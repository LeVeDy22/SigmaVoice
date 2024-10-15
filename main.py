from commands import command_dict
import speech_recognition as sr
import time
import sys
import os

recognizer = sr.Recognizer()
recognizer.pause_threshold = 0.5


def greeting():
    return "Привет! / Hello!"


def create_task():
    print("Что добавить в список дел?")
    query = listen_command()
    with open("tasks.txt", "a", encoding="utf-8") as file:
        file.write(f"⋅ {query}\n")
    return f"Задача добавлена: {query}"


def listen_command():
    try:
        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(source=mic, duration=0.5)
            print("Говорите что-то...")
            audio = recognizer.listen(source=mic)
            query = recognizer.recognize_google(audio, language="ru-RU").lower()
        return query
    except sr.UnknownValueError:
        return "Не удалось распознать речь"
    except sr.RequestError as e:
        return f"Ошибка сервиса Google Speech Recognition: {e}"


def open_browser():
    os.system("taskkill /F /IM НАЗВАНИЕ_БРАУЗЕРА.exe")
    os.startfile("ВАШ_ПУТЬ_К_БРАУЗЕРУ")
    return "Браузер открыт с сохранёнными вкладками"


def close_browser():
    os.system("taskkill /F /IM НАЗВАНИЕ_БРАУЗЕРА.exe")
    return "Браузер закрыт"


def open_youtube():
    os.system('start "" "ВАШ_ПУТЬ_К_БРАУЗЕРУ" https://www.youtube.com')
    return "YouTube открыт в новой вкладке"


def open_mindustry():
    os.startfile("ВАШ_ПУТЬ_К_МИНДАСТРИ")
    return "Игра Mindustry открыта"


def open_roblox():
    os.startfile("ВАШ_ПУТЬ_К_РОБЛОКСУ")
    return "Игра Roblox открыта"


def restart():
    os.system("shutdown /r /t 0")


def shutdown():
    os.system("shutdown /s /t 0")


def exit_program():
    sys.exit("Программа завершена.")


def calculator():
    print("Скажите выражение для вычисления (например, 2 + 2 или 3 * 4):")
    query = listen_command()
    query = (
        query.replace("умножить на", "*")
        .replace("х", "*")
        .replace("плюс", "+")
        .replace("минус", "-")
        .replace("разделить на", "/")
        .replace("поделить на", "/")
    )

    try:
        result = eval(query)
        return f"Пример: {query} = {result}"
    except Exception as e:
        return f"Ошибка вычисления: {e}"


def main():
    print(
        "Это голосовой помощник SigmaVoice. Он будет выполнять команды, сказанные вами.\n----------"
    )
    time.sleep(3)
    print("Доступные команды:")
    for key, values in command_dict["commands"].items():
        print(f"{key}: {', '.join(values)}")
    print("----------")

    while True:
        query = listen_command()
        recognized = False

        for key, values in command_dict["commands"].items():
            for value in values:
                if value in query:
                    recognized = True
                    print(globals()[key]())
                    break
            if recognized:
                break

        if not recognized:
            print(f"Не распознана команда: {query}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
