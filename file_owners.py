from collections import defaultdict

def group_by_owners(files):
    output = defaultdict(set)
    for fname, person in files.items():
        output[person].add(fname)
    return {k: list(v) for k, v in output.items()}

if __name__ == "__main__":    
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }   
    print(group_by_owners(files))
