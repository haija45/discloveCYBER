import subprocess

# Définir les commandes
commands = [
    "subfinder -dL example.txt all -recursive > subdomain.txt",
    "cat subdomain.txt | httpx -ports 80,443,8080,8000,8888 -threads 200 > subdomains_alive.txt",
    "katana -u subdomains_alive.txt -d 5 -ps -pss waybackarchive,commoncrawl,alienvault -kf -jc -fx -ef woff,css,png,svg,jpg,woff2,jpeg,gif,svg -o allurls.txt",
    'cat allurls.txt | grep -E "\\.txt|\\.log|\\.cache|\\.secret|\\.db|\\.backup|\\.yml|\\.json|\\.gz|\\.rar|\\.zip|\\.config"',
    'cat allurls.txt | grep -E "\\.js$" >> js.txt',
    'cat js.txt | while read url; do python3 /Users/wael/secretfinder/SecretFinder.py -i $url -o cli >> secret.txt; done',
    'cat secret.txt | grep -E "\\Heroku$" >> Herokykeys.txt'
]

# Exécuter les commandes séquentiellement
for command in commands:
    print(f"Executing: {command}")
    subprocess.run(command, shell=True, check=True)

print("All commands executed successfully.")

