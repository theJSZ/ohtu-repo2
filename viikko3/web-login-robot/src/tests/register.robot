*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  asdf
    Set Password  asdf1234
    Set Password Confirmation  asdf1234
    Submit Credentials
    Page Should Contain  Welcome to Ohtu Application!

Register With Too Short Username And Valid Password
    Set Username  as
    Set Password  asdf1234
    Set Password Confirmation  asdf1234
    Submit Credentials
    Page Should Contain  Username too short

Register With Valid Username And Too Short Password
    Set Username  kakka
    Set Password  as
    Set Password Confirmation  as
    Submit Credentials
    Page Should Contain  Password too short

Register With Nonmatching Password And Password Confirmation
    Set Username  aulis
    Set Password  asdf1234
    Set Password Confirmation  asfd4132
    Submit Credentials
    Page Should Contain  Password and confirmation did not match

Login After Successful Registration
    Set Username  kerkko
    Set Password  kerkko1234
    Set Password Confirmation  kerkko1234
    Submit Credentials
    Main Page
    Logout
    Set Username  kerkko
    Set Password  kerkko1234
    Login
    Title Should be  Ohtu Application main page

Login After Failed Registration
    Set Username  kurkku
    Set Password  kurkku1234
    Set Password Confirmation  kukku1234
    Submit Credentials
    Go To Login Page
    Set Username  kurkku
    Set Password  kurkku1234
    Login
    Page Should Contain  Invalid username or password    

*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Submit Credentials
    Click Button  Register

Main Page
    Click Link  ohtu

Logout
    Click Button  Logout

Login
    Click Button  Login