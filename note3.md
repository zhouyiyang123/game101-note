## __Lesson 3 变换 \(Transformation\)__

### 1\. 2D 线性变换 \(Linear Transformations\)

通常的 2D 几何变换可以通过一个 2 × 2 的矩阵与 2D 向量相乘来实现

缩放 \(Scaling\)：

```math
\begin{pmatrix}
x' \\
y'
\end{pmatrix}
=
\begin{pmatrix}
S_x&0 \\
0&S_y
\end{pmatrix}
\begin{pmatrix}
x \\
y
\end{pmatrix}
```

旋转 \(Rotation\)：绕原点逆时针旋转角度：

```math
\begin{pmatrix}
x' \\
y'
\end{pmatrix}
=
\begin{pmatrix}
cosθ&-sinθ \\
sinθ&cosθ
\end{pmatrix}
\begin{pmatrix}
x \\
y
\end{pmatrix}
```

### 2\. 齐次坐标 \(Homogeneous Coordinates\)

为什么需要齐次坐标：因为线性变换无法表示平移，平移不能写成单一矩阵相乘。

解决方案：引入第三个维度w。

2D 点表示为： 
$`
\begin{pmatrix}
x \\
y \\
1
\end{pmatrix}
`$

向量表示为：
$`
\begin{pmatrix}
x \\
y \\
0
\end{pmatrix}
`$
（向量具有平移不变性，所以w = 0可以保护向量不因平移矩	阵而改变）。

平移：
```math
\begin{pmatrix}
x' \\
y' \\
1
\end{pmatrix}
=
\begin{pmatrix}
1&0&t_x \\
0&1&t_y \\
0&0&1
\end{pmatrix}
\begin{pmatrix}
x \\
y \\
1
\end{pmatrix}
```

### 3\. 复合变换：

图形学中物体的变换往往是“先旋转、再平移”。写成矩阵乘法时，从右向左依次作用于点：$`P'=M_{translation}·M_{rotation}·P`$

复合变换结果：
```math
\begin{pmatrix}
x' \\
y' \\
1
\end{pmatrix}
=
\begin{pmatrix}
a&b&t_x \\
c&d&t_y \\
0&0&1
\end{pmatrix}
\begin{pmatrix}
x \\
y \\
1
\end{pmatrix}
```

### 4\. 三维变换：

点表示为：$`(x,y,z,1)^T`$

向量表示为：$`(x,y,z,0)^T`$

变换类似二维