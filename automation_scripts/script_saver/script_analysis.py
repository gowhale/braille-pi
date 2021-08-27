# This script finds pieces of text which are not currently voiced by a voice actor

voice_files_needed_path = "automation_scripts/script_saver/voice_files_needed.txt"

with open(voice_files_needed_path) as f:
    lines = [line.rstrip() for line in f]
    unique_lines = list(set(lines))
    print(unique_lines)

f= open("automation_scripts/script_saver/unique_lines.txt","w+")
for line in sorted(unique_lines):
    f.write("{}\n".format(line))
f.close()   
