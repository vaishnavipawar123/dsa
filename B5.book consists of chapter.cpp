/*C++ Program To read details of a book consists of chapters,
 *chapters consist of sections and sections consist of
 *subsections. Construct a tree and print the nodes.
 *Find the time and space requirements of your method.
 **/

#include <iostream>
using namespace std;

struct node {
    int chapter;
    int section;
    int subsection;
    char name[20];
    struct node* child[10];
} *root;

class tree {
public:
    void display(node* ptr);
    void insert();
    void menu();
    tree() {
        root = NULL;
    }
};

void tree::insert() {
    root = new node;
    cout << "Enter name of book : ";
    cin >> root->name;
    cout << "Enter number of chapters : ";
    cin >> root->chapter;
    for (int i = 0; i < root->chapter; i++) {
        root->child[i] = new node;
        cout << "Enter chapter " << i + 1 << " name : ";
        cin >> root->child[i]->name;
        cout << "Enter number of sections : ";
        cin >> root->child[i]->section;
        for (int j = 0; j < root->child[i]->section; j++) {
            root->child[i]->child[j] = new node;
            cout << "Enter section " << j + 1 << " name : ";
            cin >> root->child[i]->child[j]->name;
            cout << "Enter number of subsections : ";
            cin >> root->child[i]->child[j]->subsection;
            for (int k = 0; k < root->child[i]->child[j]->subsection; k++) {
                root->child[i]->child[j]->child[k] = new node;
                cout << "Enter subsection " << k + 1 << " name : ";
                cin >> root->child[i]->child[j]->child[k]->name;
            }
        }
    }
}
void tree::display(node* ptr) {
    cout << "Book : " << ptr->name << endl;
    for (int i = 0; i < ptr->chapter; i++) {
        cout << "Chapter " << i + 1 << " : " << ptr->child[i]->name << endl;
        for (int j = 0; j < ptr->child[i]->section; j++) {
            cout << "  Section " << j + 1 << " : " << ptr->child[i]->child[j]->name << endl;
            for (int k = 0; k < ptr->child[i]->child[j]->subsection; k++) {
                cout << "    Subsection " << k + 1 << " : " << ptr->child[i]->child[j]->child[k]->name << endl;
            }
        }
    }
}

void tree::menu() {
    int choice;
    while (true) {
        cout << "\nMenu:\n";
        cout << "1. Insert a new book\n";
        cout << "2. Display the current book\n";
        cout << "3. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                insert();
                break;
            case 2:
                if (root == NULL) {
                    cout << "No book exists. Please insert a book first.\n";
                } else {
                    cout << "\nCurrent book:\n";
                    display(root);
                }
                break;
            case 3:
                cout << "Exiting...\n";
                return;
            default:
                cout << "Invalid choice. Please try again.\n";
        }
    }
}

int main() {
    tree o;
    o.menu();
    return 0;
}