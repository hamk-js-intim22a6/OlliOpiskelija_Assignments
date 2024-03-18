#include <stdio.h>
#include <string.h>

int main(void)
{
    char buff[25];
    int pass = 0;

    printf("Password:\n");
    fgets(buff, sizeof(buff), stdin);
    buff[strcspn(buff, "\n")] = '\0'; // Remove trailing newline character

    if(strcmp(buff, "Secret123!xyz")) {
        printf ("Wrong Password!\n");
    }
    else {
        printf ("Correct Password\n");
        pass = 1;
    }

    if(pass) {
        /* Now Give root or admin rights to user*/
        printf ("Root privileges given.\n");
    }

    return 0;
}