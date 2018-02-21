+import math
+
+class Vector(object):
+    
+    def __init__(self, *args):
+        if len(args)==0: self.values = (0,0)
+        else: self.values = args
+        
+    def norm(self):
+        """ Returns the norm (length, magnitude) of the vector """
+        return math.sqrt(sum( comp**2 for comp in self ))
+        
+    def argument(self):
+        """ Returns the argument of the vector, the angle clockwise from +y."""
+        arg_in_rad = math.acos(Vector(0,1)*self/self.norm())
+        arg_in_deg = math.degrees(arg_in_rad)
+        if self.values[0]<0: return 360 - arg_in_deg
+        else: return arg_in_deg
+
+    def normalize(self):
+        """ Returns a normalized unit vector """
+        norm = self.norm()
+        normed = tuple( comp/norm for comp in self )
+        return Vector(*normed)
+    
+    def rotate(self, *args):
+        """ Rotate this vector. If passed a number, assumes this is a 
+            2D vector and rotates by the passed value in degrees.  Otherwise,
+            assumes the passed value is a list acting as a matrix which rotates the vector.
+        """
+        if len(args)==1 and type(args[0]) == type(1) or type(args[0]) == type(1.):
+            # So, if rotate is passed an int or a float...
+            if len(self) != 2:
+                raise ValueError("Rotation axis not defined for greater than 2D vector")
+            return self._rotate2D(*args)
+        elif len(args)==1:
+            matrix = args[0]
+            if not all(len(row) == len(v) for row in matrix) or not len(matrix)==len(self):
+                raise ValueError("Rotation matrix must be square and same dimensions as vector")
+            return self.matrix_mult(matrix)
+        
+    def _rotate2D(self, theta):
+        """ Rotate this vector by theta in degrees.
+            
+            Returns a new vector.
+        """
+        theta = math.radians(theta)
+        # Just applying the 2D rotation matrix
+        dc, ds = math.cos(theta), math.sin(theta)
+        x, y = self.values
+        x, y = dc*x - ds*y, ds*x + dc*y
+        return Vector(x, y)
+       
