# Log-In-and-Sign-Up-Python-Program
This is a very basic Log In and Sig Up program. It stores the password and email mixed together in a SHA-1 hash format in a separate file.

      'UUID' and 'getpass' modules are imported.
            UUID will encrypt the email mixed with the password in a .txt file.
            getpass will hide the password when it is inputed during Log In and Sign Up.

      A 'useless_loop' will be set as true
            While this loop is True
                  The user will be asked to enter a command (line 7)
                  
                        If the command is 'print functions' (line 9)
                              All the commands that the program has to offer will be printed (line 10)
                              
                        If the command is 'new' (line 16)
                              user will be asked to set sign up credentials
                                    If the email is not found in the .txt file
                                          A string containing 'email + password' will be created (line 23)
                                          The string of line 23 will be hashed (line 24)
                                          'plain email + (hashed email + hashed password)' will be saved in a .txt file (line 25)
                                    Else 'Email alredy stored!' will be printed
                                    
                        If the command is 'log in' (line 31)
                              User will be asked to enter email (line 32)
                              If the email if found in the .txt file (line 33 & 34 will check for the email in the .txt file)
                                    The user will be asked to enter the password (line 35)
                                    The credentials will be hashed using the same formula as on the Sign Up
                                    Program will check for the mixed string in the .txt file (line 39)
                              Else 'Wrong email!' will be printed (line 44)
                              
                        If 'çlose' or 'exit ' is inputed in the command request on line 7 (line 46)
                              The 'useless_loop' will be set as False and the whole loop will break closing the program
                              
                        Else 'Try Again!' will be printed (line 48)
