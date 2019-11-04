## Uso de branchs en git

1. Crear una nueva branch y cambiar `git checkout -b <branch-name>`
2. Commits...
3. Nos "paramos" en master `git checkout master`
4. `git merge <branch-name>`
*Lo más probable es que hagamos un [Fast Forward Merge](https://www.atlassian.com/git/tutorials/using-branches/git-merge)*
5. `git branch -d <branch-name>` (Borrado local)
6. `git push <remote-name> :<branch-name>`
Ejemplo: `git push origin :caracteristicas`