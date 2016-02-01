#!/bin/bash

# Since we are testing the different capabilities of ownership commands,
# we will execute this as root since the VMs I gave you only have one user
if [[ $(id -u) -ne 0 ]]; then
    echo "You must execute this script as the root user..."
    echo "...try typing this:"
    echo ""
    echo "    sudo gen_demo.sh"
    echo ""
    exit 0
fi

# Now that we are executing as root, let's go ahead and create the demo folder and a
# few files to check the permissions on

# I have intentionally split the -d and -f checks here purely for demonstrative purposes
# of how to setup an if -- elif --fi block in bash.
#
# Realistically, you would want to use -e for greater safety.  I made the relatively safe
# assumption that none of you have block devices in the same directory as this script ;)
#
# Refer to this for the file checks: http://tldp.org/LDP/abs/html/fto.html

# I scraped the deletion prompt from this excellent response:
#
#     http://stackoverflow.com/a/3232082/3814202
#
# I hope you realize now that I strongly endorse using the internet to solve problems,
# so long as you are explicit in citing what you have taken from where!

# If the demo directory exists, make sure we can delete it
if [[ -d "demo" ]]; then
    echo "(!) The demo folder already exists (!)"
    echo ""
    read -r -p "Can I delete it? [y/N] " response
    case $response in
        [yY][eE][sS]|[yY])
            rm -rf demo/
            ;;
        *)
            # User responded with a no, or invalid answer
            echo "Ok, I'll let you do that instead.  Run this script again when you are ready."
            exit 0
            ;;
    esac
# A file named demo exists here for some reason, confirm deletion
elif [[ -f "demo" ]]; then
    echo "(!) A file named <demo> already exists (!)"
    echo ""
    read -r -p "Can I delete it? [y/N] " response
    case $response in
        [yY][eE][sS]|[yY])
            rm -f demo
            ;;
        *)
            # User responded with a no, or invalid answer
            echo "Ok, I'll let you do that instead.  Run this script again when you are ready."
            exit 0
            ;;
    esac
fi

# Now we are able to create some folders and files as the root user to test using ownership commands!
mkdir demo
chmod 775 demo/
mkdir demo/lemmings
chmod 444 demo/lemmings/ # these are extraordinarily bad folder permissions...
touch demo/lemmings/are_watching_you.txt
echo "from behind!!!" > demo/lemmings/are_watching_you.txt
chmod ugo-rwx demo/lemmings/are_watching_you.txt

echo "Your playground has been constructed!  Follow the directions in the README."

