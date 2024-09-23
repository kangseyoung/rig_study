import re
import sys
sys.path.append('D:\maya_rig_test')
import maya.cmds as cmds
import fnmatch

class MeshFinder():
    """
    The MeshFinder class provides utility functions to find meshes based on 
    their name or pattern and also retrieve the top-level group of a given node.
    """

    def find_meshes_with_name(self, pattern):
        """
        Finds meshes based on the provided name pattern using wildcards.
        
        :param pattern: Name pattern with wildcards (e.g., "*_pelvis").
        :rtype: list
        :return: List of matching mesh names.
        """
        print(f"Searching for meshes with the name pattern: {pattern}")
        all_meshes = cmds.ls(type='mesh', long=True)
        print(f"All meshes found in the scene: {all_meshes}")
        matching_meshes = fnmatch.filter(all_meshes, pattern)
        if matching_meshes:
            print(f"Matching meshes found: {matching_meshes}")
        else:
            print("No matching meshes found, returning 'root'")
        return matching_meshes if matching_meshes else "root"
            
    def find_meshes_with_pattern(self, pattern):
        """
        Finds meshes whose names match the given regular expression pattern.
        
        :param pattern: Regular expression pattern to search for in mesh names.
        :rtype: list or None
        :return: A list of matching mesh names or None if no matches are found.
        """
        print(f"Searching for meshes matching the regex pattern: {pattern}")
        all_meshes = cmds.ls(type='mesh', long=True)
        print(f"All meshes found in the scene: {all_meshes}")
        match_meshes = []
        for mesh in all_meshes:
            if re.search(pattern, mesh):
                print(f"Mesh matching pattern found: {mesh}")
                match_meshes.append(mesh)
        if match_meshes:
            print(f"Meshes matching the pattern: {match_meshes}")
        else:
            print("No meshes matching the pattern found.")
        return match_meshes if match_meshes else None

    def get_top_level_group(self, node):
        """
        Recursively finds the top-level group (root group) for the given node.
        
        :param node: Node or mesh for which to find the top-level group.
        :rtype: str
        :return: The name of the top-level group.
        """
        print(f"Finding top-level group for node: {node}")
        parent = cmds.listRelatives(node, parent=True)
        if not parent:
            print(f"Top-level group for {node}: {node}")
            return node
        print(f"Parent of {node}: {parent[0]}")
        return self.get_top_level_group(parent[0])
