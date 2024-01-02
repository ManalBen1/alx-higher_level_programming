#include <stdio.h>
#include <stdlib.h>
int main()
{
char* pythonScript = getenv("PYFILE");
if (pythonScript == NULL)
{
return (1);
}

char command[100];
snprintf(command, sizeof(command), "python3 %s", pythonScript);
return system(command);
}
