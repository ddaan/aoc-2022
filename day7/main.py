class Directory:

    def __init__(self, name='', parent=None) -> None:
        self.name = name
        self.parent = parent
        self.files = []
        self.directories = []
        self.total_size = 0

    def add_file_line(self, line):
        l, r = line.split(' ')
        if l == 'dir':
            self.add_directory(r)
        else:
            self.files.append(File(name=r, size=l))

    def add_directory(self, name):
        try:
            return [d for d in self.directories if d.name == name][0]
        except:
            new_directory = Directory(name=name, parent=self)
            self.directories.append(new_directory)
            return new_directory

    def print_tree(self, indent=0):
        print(' '* indent + '- '+ self.name + f' (TOTAL SIZE: {self.get_total_size_including_subs()})')
        for directory in self.directories:
            directory.print_tree(indent+4)

        self.print_files(indent+4)
        self.total_size = self.get_total_size_including_subs()

    def print_files(self, indent):
        for file in self.files:
            print (' '*indent + file.name + ' ' + file.size)

    def get_total_size(self):
        return sum([int(f.size) for f in self.files])

    def get_total_size_including_subs(self):
        size = self.get_total_size()
        for directory in self.directories:
            size += directory.get_total_size_including_subs()

        return size

    def get_all_sizes_until_100000(self):
        rlist = []
        if self.total_size < 100000:
            rlist = [self.total_size]

        for directory in self.directories:
            rlist.extend(directory.get_all_sizes_until_100000())

        return rlist

    def get_directory_to_delete(self, free_space, needed):
        rlist = []
        if (free_space - self.total_size) < needed:
            rlist = [self.total_size]

        for directory in self.directories:
            rlist.extend(directory.get_directory_to_delete(free_space, needed))

        return rlist

class File:
    def __init__(self, name='', size='') -> None:
        self.name = name
        self.size = size

class FileSystem():

    def __init__(self) -> None:
        self.fs = {}
        self.files = []
        self.mode = ''
        self.main_directory = Directory(name='/')
        self.current_directory = self.main_directory
        self.lvl = 0

    def parse_input(self, line):
        if line[0] == '$':
            commands = line.split(' ')
            if commands[1] == 'cd':
                if commands[2] == '/':
                    self.current_directory = self.main_directory
                elif commands[2] == '..':
                    self.current_directory = self.current_directory.parent
                else:
                    self.current_directory = self.current_directory.add_directory(commands[2])
        else:
            self.current_directory.add_file_line(line)

    def print_tree(self):
        self.main_directory.print_tree()

    def get_all_sizes_until_100000(self):
        sizes = self.main_directory.get_all_sizes_until_100000()
        print(sizes)
        print(sum(sizes))

    def get_directory_to_delete(self, disk_size, total_needed):
        free_space = disk_size - self.main_directory.total_size
        needed = total_needed - free_space
        directories = self.main_directory.get_directory_to_delete(free_space, needed)
        print('\n Directory sizes that can be deleted to get to {needed} bytes')
        print (directories)
        print(min(directories))

def input_for_test():
    return """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

def get_file(name):
    with open(name) as file:
        lines = file.readlines()
    return lines


def main():
    fs = FileSystem()
    test_input = input_for_test()

    for line in test_input.split('\n'):
        fs.parse_input(line)

    fs.print_tree()
    fs.get_all_sizes_until_100000()
    fs.get_directory_to_delete(70000000, 30000000)
    import pdb; pdb.set_trace()

    #### task 1 ###

    fs = FileSystem()
    input = get_file('input')

    for line in input:
        fs.parse_input(line.strip())

    fs.print_tree()
    fs.get_all_sizes_until_100000()
    fs.get_directory_to_delete(70000000, 30000000)


if __name__ == "__main__":
    main()