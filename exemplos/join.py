import threading
import requests

# URL dos arquivos para download
urls = [
    "https://example.com/file1.txt",
    "https://example.com/file2.txt",
    "https://example.com/file3.txt",
    "https://example.com/file4.txt"
]

# Função que realiza o download de um arquivo
def download_file(url):
    response = requests.get(url)
    filename = url.split("/")[-1]
    
    with open(filename, "wb") as file:
        file.write(response.content)
    
    print("Download concluído:", filename)

# Criação das threads para cada download
threads = []
for url in urls:
    thread = threading.Thread(target=download_file, args=(url,))
    threads.append(thread)
    thread.start()

# Aguarda a conclusão de cada download usando join()
for thread in threads:
    thread.join()

print("Todos os downloads foram concluídos.")