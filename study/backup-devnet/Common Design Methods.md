# Model-View-Controller (MVC)
## SoC Principle
- Separation of Concerns (SoC)
- Design principle for modular coding
- Upgrading of modular code components
- Separate back-end and front-end code

## Model
Data Management
- Single file or Database (most commonly db)
- Performing actions against data
	- Select, update, insert, delete

## View
User Interface (UI)
- Web browser or CLI
- Presents urrent data state

## Controller
Brains
- Passes user requests
![[Pasted image 20240120134008.png]]
- User requests to see specific data view the view, which hits the controller, which sends the request to the model.  The model returns the information to the controller, which sends it back to the view (UI)

## MVC Advantages
- Ability to implement SoC
- Allows for smaller functions and components
- Easier collaboration among devs

# Observer
- one-to-many relationships
- An object is accessed by many programs or individuals
- Consists of a subject and one or more observers
- Subscription-based model
- Social media platforms are an example
- "One" = status update
- "Many" = followers receiving notification

## Observer pattern
- Obtain real-time data due to notifications
- Contrasts with polling intervals
- Used within the MVC pattern to update views


# Version Control
- Tracking changes to a file or a set of files
- Software tools track changes for historical perspective
- Important for collaboration purposes

## Git Version Control System
- Central server as a repository of data
- Multiple entities can have working copies
- E.g. GitHub
- **Advantages**
	- Historical versioning of code
	- Comparison between earlier versions
	- Ideal for collaboration amongst teams
	- Easily branch or merge code as needed
- Most popular version control system
- Git is not the same as GitHub
	- Github uses Git
- 