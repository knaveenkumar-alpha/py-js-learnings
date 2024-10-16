"""
Browser history management can be represented using both **stacks** and **doubly linked lists**, 
depending on the specific aspect of navigation being considered:

### 1. **Stack Representation**
- **Scenario**: Moving Back and Forward
- **Explanation**: When you navigate between pages in a browser, the actions are typically stored in 
    two separate stacks:
  - The **"Back Stack"** keeps track of the pages you have visited.
  - When you press the back button, the current page is moved from the **back stack** to a **"Forward Stack"**.
  - Pressing the forward button pops a page from the forward stack and puts it back on the back stack.
- **Real-World Example**: This setup allows the browser to maintain a history of your navigation such that you 
    can undo and redo navigation actions, just like in a text editor's undo/redo functionality.
  
### 2. **Doubly Linked List Representation**
- **Scenario**: Full Browser Navigation
- **Explanation**: For a complete representation of the browser history, a **doubly linked list** is a more 
    suitable structure because it allows:
  - **Bi-directional traversal** (i.e., you can navigate forward and backward easily).
  - **Insertion of new nodes** (web pages) anywhere in the history when a new page is visited.
  - Each node in the doubly linked list stores a reference to the previous and next nodes, making it easy to manage 
    history traversal in either direction.
- **Real-World Example**: When you visit a new page after using the back button, the "forward" history is removed. 
    This operation is easier to manage in a doubly linked list because you can easily cut off the tail part of the 
        list and add a new node.

### **Conclusion**
- **If focusing on back and forward navigation**: The stack-based approach models this effectively because each action 
    (back or forward) is akin to pushing and popping from separate stacks.
- **If considering the entire browser history with the ability to add/remove pages from the middle**:
    A **doubly linked list** is a better fit, as it allows for efficient navigation and modification of the history 
    in both directions.

So, **both data structures** are used for different purposes in browser history management, but the complete history
    management (with bidirectional navigation) is best represented as a **doubly linked list** in the real world.
"""