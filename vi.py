import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to take dataset input from the user
def get_dataset():
    file_path = input("Enter the file path of your dataset: ")
    # Assuming the dataset is in CSV format for simplicity
    dataset = pd.read_csv(file_path)
    # Convert object datatype to string or int
    for column in dataset.columns:
        if dataset[column].dtype == 'object':
            try:
                dataset[column] = dataset[column].astype(int)
            except ValueError:
                dataset[column] = dataset[column].astype(str)
    return dataset

# Function to print column names with indices
def print_columns_with_indices(dataset):
    print("Columns in the dataset:")
    for i, column in enumerate(dataset.columns):
        try:
            print(f"{i+1}] {column} ({dataset[column].dtype})")
        except Exception as e:
            print(f"Error: {e}")

# Function to select columns X and Y from the dataset
def select_columns(dataset):
    print("Select columns X and Y from the dataset:")
    print_columns_with_indices(dataset)
    while True:
        try:
            x_index = int(input("Enter the index of column X (string type): ")) - 1
            y_index = int(input("Enter the index of column Y (integer type): ")) - 1
            z_index = input("Enter the index of column Z (string type, enter blank if not needed): ").strip()
            return dataset.columns[x_index], dataset.columns[y_index], dataset.columns[int(z_index) - 1] if z_index else None
        except ValueError:
            print("Invalid input. Please enter a valid index.")
        except IndexError:
            print("Index out of range. Please enter a valid index.")
        except Exception as e:
            print(f"Error: {e}")

# Function to create various types of charts
def create_chart(dataset, x_column, y_column, z_column):
    print("Select the type of chart:")
    print("1] Bar graph (int vs string)")
    print("2] Count plot (int vs string)")
    print("3] Pie chart (int vs int")
    print("4] Heatmap (int vs int vs int)")
    print("5] Scatter plot (int vs int)")
    print("6] Line plot (int vs int)")
    print("7] Histogram (int vs int)")
    print("8] Box plot (int vs int)")
    print("9] Distribution plot (int vs int)")

    chart_type = int(input("Enter your choice: "))

    if chart_type == 1:
        plt.figure(figsize=(10, 6))
        sns.barplot(x=x_column, y=y_column, data=dataset)
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.title("Bar Graph")
        plt.xticks(rotation=45)
        plt.show()

    elif chart_type == 2:
        plt.figure(figsize=(10, 6))
        sns.countplot(x=x_column, data=dataset)
        plt.xlabel(x_column)
        plt.ylabel('Count')
        plt.title("Count Plot")
        plt.xticks(rotation=45)
        plt.show()
    
    elif chart_type == 3:
        plt.figure(figsize=(8, 8))
        plt.pie(dataset[y_column], labels=dataset[x_column], autopct='%1.1f%%')
        plt.title("Pie Chart")
        plt.axis('equal')
        plt.show()

    elif chart_type == 4:
        plt.figure(figsize=(10, 8))
        sns.heatmap(dataset[[x_column, y_column]].corr(), annot=True, cmap='coolwarm', fmt='.2f')
        plt.title("Heatmap")
        plt.show()
    
    elif chart_type==5:
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x=x_column, y=y_column, data=dataset)
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.title("Scatter Plot")
        plt.show()
    
    elif chart_type==6:
        plt.figure(figsize=(10, 6))
        sns.lineplot(x=x_column, y=y_column, data=dataset)
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.title("Line Plot")
        plt.show()

    elif chart_type==7:
        plt.figure(figsize=(10, 6))
        sns.histplot(x=x_column, y=y_column, data=dataset)
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.title("Histogram")
        plt.show()

    elif chart_type==8:
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=x_column, y=y_column, data=dataset)
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.title("Box Plot")
        plt.show()
    
    elif chart_type==9:
        plt.figure(figsize=(10,6))
        sns.distplot(dataset[y_column], bins=20)
        plt.xlabel(y_column)
        plt.ylabel('Density')
        plt.title("Distribution Plot")
        plt.show() 
   
    else:
        print("Invalid choice. Please select a choice.")

# Main function to orchestrate the process
def main():
    dataset = get_dataset()
    x_column, y_column, z_column = select_columns(dataset)
    create_chart(dataset, x_column, y_column, z_column)
    
if __name__ == "__main__":
    main()