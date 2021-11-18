*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User  jussi  jussi111

*** Test Cases ***
Register With Valid Username And Password
    Input New Command And Create User  kerkko  kerkko111
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input New Command And Create User  jussi  jussi123
    Output Should Contain  User with username jussi already exists

Register With Too Short Username And Valid Password
    Input New Command And Create User  jr  jussi123
    Output Should Contain  Username too short

Register With Valid Username And Too Short Password
    Input New Command And Create User  kerkko  asd
    Output Should Contain  Password too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command And Create User  kerkko  passwordaaa
    Output Should Contain  Invalid password
    
*** Keywords ***
Input New Command And Create User
    [Arguments]  ${username}  ${password}
    Input New Command
    Input Credentials  ${username}  ${password}