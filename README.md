# PyWdHasher
Password hashing python port
A python script for creating seemingly random passwords, based on a known website and a personal key.

## Usage

Copy the websites domain and execute the bash script

  $> bash bin/passwordhasher.sh

The password generator will read the domain from the clipboard and ask you for a secret. These are then used by a cryptographic hashing algorithm to generate a 32 character long password, which is then injected to the clipboard.

You should then be able to paste you password directly into password fields.

The cryptographic hashing algorithm is a one-way hashing algorithm, meaning that the outcome will always be the same, if the same website domain and secret has been used.

### Options

The password generator accepts arguments that can mutate the generated password. This allows you to, say, truncate the generated password to a certain length, if the website administrator doesn't care about you and stores password in cleartext. You can also replace ordinairy alphanumeric characters with special characters, if the website administrator thinks it makes your password harder to bruteforce.

## Cli arguments

Currently the most updated documentation is in the code