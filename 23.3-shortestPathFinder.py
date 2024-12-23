import sys
import queue
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QGridLayout
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QFont

# Define the maze
maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]

class MazeWidget(QWidget):
    def __init__(self):
        super().__init__()
        #self.setStyleSheet("background-color: black;")
        self.setWindowOpacity(0.9) #Transparency
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Maze Path Finder')
        self.setGeometry(100, 100, 600, 400)

        # Set up dark background
        self.setStyleSheet("background-color: #2E2E2E;")  # Dark gray background

        # Create a grid layout for the maze
        self.gridLayout = QGridLayout()
        self.setLayout(self.gridLayout)

        # Create QLabel for each cell in the maze
        self.labels = {}
        for row in range(len(maze)):
            for col in range(len(maze[row])):
                label = QLabel(maze[row][col])
                label.setAlignment(Qt.AlignCenter)
                label.setFont(QFont('Courier', 14))
                
                # Set default color for each cell based on its value
                if maze[row][col] == "#":
                    label.setStyleSheet("color: lightblue;")  # Light blue color for '#'
                elif maze[row][col] == "X":
                    label.setStyleSheet("color: lightcoral;")  # Light red color for 'X'
                else:
                    label.setStyleSheet("color: white;")  # White color for empty spaces

                self.gridLayout.addWidget(label, row, col)
                self.labels[(row, col)] = label

        # Set up a QTimer to animate the path finding
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateMaze)
        self.paths = []  # Store all explored paths
        self.current_step = 0

        # Find the paths and start the animation
        self.find_paths()
        self.timer.start(500)  # Update every 500ms

    def updateMaze(self):
        if self.current_step < len(self.paths):
            # Clear previous 'X' marks
            self.clear_path_marks()

            path = self.paths[self.current_step]
            for row, col in path:
                self.labels[(row, col)].setText('X')
                self.labels[(row, col)].setStyleSheet("color: lightcoral;")  # Update color for 'X'
            self.current_step += 1
        else:
            self.timer.stop()

    def clear_path_marks(self):
        # Reset cells to their original state (empty space or walls)
        for (row, col), label in self.labels.items():
            if maze[row][col] == " ":
                label.setText(" ")
                label.setStyleSheet("color: white;")  # Reset color for empty spaces
            elif maze[row][col] == "#":
                label.setText("#")
                label.setStyleSheet("color: lightblue;")  # Light blue color for '#'
            elif maze[row][col] == "X":
                label.setStyleSheet("color: lightcoral;")  # Light red color for 'X'
    
    def find_paths(self):
        start = "O"
        end = "X"
        start_pos = self.find_start(start)
        q = queue.Queue()
        q.put((start_pos, [start_pos]))

        visited = set()
        all_paths = []  # Store all paths found
        temp_paths = []  # Store intermediate paths for visualization

        while not q.empty():
            current_pos, path = q.get()
            row, col = current_pos

            if maze[row][col] == end:
                all_paths.append(path)
                temp_paths.append(path)
                continue  # Continue searching for other paths

            neighbors = self.find_neighbors(row, col)
            for neighbor in neighbors:
                if neighbor in visited:
                    continue
                r, c = neighbor
                if maze[r][c] == "#":
                    continue
                new_path = path + [neighbor]
                q.put((neighbor, new_path))
                visited.add(neighbor)
                temp_paths.append(new_path)

        self.paths = temp_paths

    def find_start(self, start):
        for i, row in enumerate(maze):
            for j, value in enumerate(row):
                if value == start:
                    return i, j
        return None

    def find_neighbors(self, row, col):
        neighbors = []
        if row > 0:  # UP
            neighbors.append((row - 1, col))
        if row + 1 < len(maze):  # DOWN
            neighbors.append((row + 1, col))
        if col > 0:  # LEFT
            neighbors.append((row, col - 1))
        if col + 1 < len(maze[0]):  # RIGHT
            neighbors.append((row, col + 1))
        return neighbors

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MazeWidget()
    widget.show()
    sys.exit(app.exec_())
