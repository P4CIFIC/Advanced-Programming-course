class FriendFinder():
    def __init__(self, number_of_test_cases) -> None:
        self.number_of_test_cases = number_of_test_cases
    
    def get_numbers_from_line(self, line):
        self.line = line.split(" ")
        return int(self.line)
    
    def get_all_datasets(self):
        while self.number_of_test_cases > 0:
            self.number_of_pairs = self.get_numbers_from_line(input())[1]

            
        
        
            