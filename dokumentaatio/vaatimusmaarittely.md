# Requirements Specification

## Purpose of the Application

The application allows users to create and manage _Dungeons & Dragons_ characters. It provides a character creation tool where the user can define a character's race, class, background, and ability scores, and save characters for later use. The application supports multiple registered users, each with their own individual character library.

## Users

Initially the application has only one user role, a _normal user_. Later, an _admin user_ with elevated privileges may be added.

## UI Sketch

tbd

The application opens to a login view, from which the user can navigate to a new user registration view, or upon successful login, to their character library.

## Core Functionality

### Before Logging In

- A user can create an account
  - The username must be unique and at least 5 characters long
- A user can log in
  - Login succeeds by entering an existing username and password in the login form
  - If the user does not exist or the password does not match, the system notifies the user

### After Logging In

- The user can view their character library, i.e. their saved _characters_
- The user can create a new character
  - The character is given a name, race, class, and background
  - Ability scores (STR, DEX, CON, INT, WIS, CHA) can be entered manually or rolled randomly
  - A created character is visible only to the user who created it
- The user can view the details of an individual character
- The user can delete a character from their library
- The user can log out

## Ideas for Further Development

After the core version, the system may be extended with the following features as time allows:

- Editing character details after creation
- Exporting a character as a text file or other format (tbd)
- Managing a character's skills and equipment
- Level progression and the associated changes to character stats
- Sorting and filtering characters by class or race
- Sharing a character with other users
- Campaign management, where multiple characters can be grouped under a shared campaign
- Deleting a user account and all associated characters