import subprocess as sp
import csv


resources = ['google.com', 'ya.ru', 'liquipedia.net', 'mail.ru', 'nsu.ru', 
            'github.com', '0.0.0.0', 'vk.com', 'gmail.com', 'quora.com']

with open('ping_statistics.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ['resource', 'rtt']
    writer.writerow(field)

    for resource in resources:
        command = f"ping -c 1 {resource} | grep \"rtt\" --color=never"
        result = sp.run(command, capture_output=True, shell=True)
        result_parsed = result.stdout.decode().strip()
        if not result_parsed:
            result_parsed = "NaN"

        writer.writerow([resource, result_parsed])
