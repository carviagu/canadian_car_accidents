# Configuration Information

Información sobre el entorno de conda que se utiliza en el proyecto y el estilo de los jupyter notebooks. 

### Contenido
1. Environment
2. Notebooks

---

<br>

## Environment
Utilizamos un entorno de anaconda.
```
conda create --name ML_P1
```
Instalamos el kernel y los paquetes a utilizar.
```
conda activate ML_P1
conda install ipykernel
```
Se puede encontrar más información sobre la gestión de entornos en https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html

### Paquetes (rev. 01/12/2021)
* Pandas: https://anaconda.org/anaconda/pandas
* Numpy: https://anaconda.org/anaconda/numpy
* Seaborn: https://anaconda.org/anaconda/seaborn
* Matplotlib: https://anaconda.org/conda-forge/matplotlib
* Nbconvert: https://anaconda.org/anaconda/nbconvert
* OS: https://anaconda.org/jmcmurray/os

<br>

## Notebooks
Se utiliza una plantillas estándar para crear los notebooks, de tal forma que sigan una misma estructura y estilo. De tal forma que se encuentre todo organizado de manera similar. 
Pantilla base: ```notebooks/templates/template.ipynb```.
