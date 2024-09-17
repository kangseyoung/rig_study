
import re
import maya.cmds as cmds
from get_joint_position import PositionCollector, MeshFinder

class JointPosCatcher(PositionCollector, MeshFinder):
    """
    The JointPosCatcher class calculates joint positions by referencing mesh objects.
    It inherits from PositionCollector and MeshFinder to extend its functionality 
    and calculate different joint positions within the rigging pipeline.
    """
    
    
    ####################################################################
    # root
    def get_root_joint_pos(self):
        """
        Returns the root joint position.
        
        :rtype: tuple
        :return: Tuple representing the root joint position at (0, 0, 0)
        """
        p = (0, 0, 0)
        return p

    ####################################################################
    # main
    def get_main_joint_pos(self):
        """
        Retrieves the position of the 'pelvis' mesh and calculates its half position.
        
        :rtype: tuple
        :return: Tuple representing the half position of the 'pelvis' mesh
        """
        mesh = self.find_meshes_with_name("*_pelvis")
        p = self.get_half_positions(mesh)
        return p

    ####################################################################
    # body
    def get_spine1_joint_pos(self):
        """
        Retrieves the position of the 'spine1' mesh and calculates its half position.
        
        :rtype: tuple
        :return: Tuple representing the half position of the 'spine1' mesh
        """
        mesh = self.find_meshes_with_name("*_spine1")
        p = self.get_half_positions(mesh)
        return p

    def get_spine2_joint_pos(self):
        """
        Retrieves the position of the 'spine2' mesh and calculates its half position.
        
        :rtype: tuple
        :return: Tuple representing the half position of the 'spine2' mesh
        """
        mesh = self.find_meshes_with_name("*_spine2")
        p = self.get_half_positions(mesh)
        return p

    def get_spine3_joint_pos(self):
        """
        Retrieves the position of the 'spine3' mesh and calculates its half position.
        
        :rtype: tuple
        :return: Tuple representing the half position of the 'spine3' mesh
        """
        mesh = self.find_meshes_with_name("*_spine3")
        p = self.get_half_positions(mesh)
        return p

    def get_neck_joint_pos(self):
        """
        Retrieves the position of the 'neck' mesh and calculates its bottom center position.
        
        :rtype: tuple
        :return: Tuple representing the bottom center position of the 'neck' mesh
        """
        mesh = self.find_meshes_with_name("*_neck")
        p = self.get_pos_bottom_center(mesh)
        return p

    def get_head_joint_pos(self):
        """
        Retrieves the position of the 'head' mesh and calculates its bottom center position.
        
        :rtype: tuple
        :return: Tuple representing the bottom center position of the 'head' mesh
        """
        mesh = self.find_meshes_with_name("*_head")
        p = self.get_pos_bottom_center(mesh)
        return p

    ####################################################################
    # arms
    def get_clavicle_joint_pos(self):
        """
        Retrieves the position of the 'spine3' mesh and calculates its quarter top position.
        
        :rtype: tuple
        :return: Tuple representing the quarter top position of the 'spine3' mesh
        """
        mesh = self.find_meshes_with_name("*_spine3")
        p = self.get_pos_quater_top_(mesh)
        return p

    def get_shoulder_joint_pos(self):
        """
        Retrieves the position of the 'L_shoulder' mesh and calculates its half position.
        
        :rtype: tuple
        :return: Tuple representing the half position of the 'L_shoulder' mesh
        """
        mesh = self.find_meshes_with_name("*_L_shoulder")
        p = self.get_half_positions(mesh)
        return p

    def get_elbow_joint_pos(self):
        """
        Retrieves the position of the 'L_elbow' mesh and calculates its half position.
        
        :rtype: tuple
        :return: Tuple representing the half position of the 'L_elbow' mesh
        """
        mesh = self.find_meshes_with_name("*_L_elbow")
        p = self.get_half_positions(mesh)
        return p

    def get_wrist_joint_pos(self):
        """
        Retrieves the position of the 'L_wrist' mesh and calculates its half position.
        
        :rtype: tuple
        :return: Tuple representing the half position of the 'L_wrist' mesh
        """
        mesh = self.find_meshes_with_name("*_L_wrist")
        p = self.get_half_positions(mesh)
        return p

    def get_hand_joint_pos(self):
        """
        Retrieves the position of the 'L_hand' mesh and calculates its half position.
        
        :rtype: tuple
        :return: Tuple representing the half position of the 'L_hand' mesh
        """
        mesh = self.find_meshes_with_name("*_L_hand")
        p = self.get_half_positions(mesh)
        return p

    ####################################################################
    # fingers
    def get_thumb_joints_pos(self):
        """
        Finds meshes with the name 'thumb' and calculates their half positions.
        Returns the positions as a tuple.
        
        :rtype: tuple
        :return: Tuple containing the half positions of all thumb joints
        """
        pattern = r".*thumb\d$"
        meshes = self.find_meshes_with_pattern(pattern)
        p_list = []
        for mesh in meshes:
            p = self.get_half_positions(mesh)
            p_list.append(p)
        p_tuple = tuple(p_list)
        return p_tuple

    def get_index_joints_pos(self):
        """
        Finds meshes with the name 'index' and calculates their half positions.
        Returns the positions as a tuple.
        
        :rtype: tuple
        :return: Tuple containing the half positions of all index joints
        """
        pattern = r".*index\d$"
        meshes = self.find_meshes_with_pattern(pattern)
        p_list = []
        for mesh in meshes:
            p = self.get_half_positions(mesh)
            p_list.append(p)
        p_tuple = tuple(p_list)
        return p_tuple

    def get_picky_joints_pos(self):
        """
        Finds meshes with the name 'picky' and calculates their half positions.
        Returns the positions as a tuple.
        
        :rtype: tuple
        :return: Tuple containing the half positions of all picky joints
        """
        pattern = r".*picky\d$"
        meshes = self.find_meshes_with_pattern(pattern)
        p_list = []
        for mesh in meshes:
            p = self.get_half_positions(mesh)
            p_list.append(p)
        p_tuple = tuple(p_list)
        return p_tuple

    ####################################################################
    # legs
    def get_but_joint_pos(self):
        """
        Retrieves the position of the 'L_but' mesh and calculates its half position.
        
        :rtype: tuple
        :return: Tuple representing the half position of the 'L_but' mesh
        """
        mesh = self.find_meshes_with_name("*_L_but")
        p = self.get_half_positions(mesh)
        return p

    def get_knee_joint_pos(self):
        """
        Retrieves the position of the 'L_knee' mesh and calculates its half position.
        
        :rtype: tuple
        :return: Tuple representing the half position of the 'L_knee' mesh
        """
        mesh = self.find_meshes_with_name("*_L_knee")
        p = self.get_half_positions(mesh)
        return p

    def get_ankle_joint_pos(self):
        """
        Retrieves the position of the 'L_ankle' mesh and calculates its half position.
        
        :rtype: tuple
        :return: Tuple representing the half position of the 'L_ankle' mesh
        """
        mesh = self.find_meshes_with_name("*_L_ankle")
        p = self.get_half_positions(mesh)
        return p

    def get_foot_joint_pos(self):
        """
        Retrieves the position of the 'L_foot' mesh and calculates the bottom center minimum Z position.
        
        :rtype: tuple
        :return: Tuple representing the bottom minimum Z position of the 'L_foot' mesh
        """
        mesh = self.find_meshes_with_name("*_L_foot")
        p = self.get_pos_bottom_minz_center(mesh)
        return p

    def get_toe_joint_pos(self):
        """
        Retrieves the position of the 'L_toe' mesh and calculates the bottom center maximum Z position.
        
        :rtype: tuple
        :return: Tuple representing the bottom maximum Z position of the 'L_toe' mesh
        """
        mesh = self.find_meshes_with_name("*_L_toe")
        p = self.get_pos_bottom_maxz_center(mesh)
        return p
    
class PositionCollector():
    """
    The PositionCollector class provides utility functions to calculate positions
    of various mesh objects based on their bounding box, such as half positions, 
    quarter positions, and other custom points like bottom center or top quarter.
    """

    def get_pos_bottom_center(self, mesh):
        """
        Calculates the bottom center position of the given mesh.
        
        :param mesh: Mesh object to calculate position from.
        :rtype: tuple
        :return: Tuple representing the bottom center position (min_y, center_x, center_z)
        """
        bbox = cmds.exactWorldBoundingBox(mesh)
        min_x, min_y, min_z, max_x, max_y, max_z = bbox
        center_x = (min_x + max_x) / 2
        center_z = (min_z + max_z) / 2
        return (min_y, center_x, center_z)

    def get_pos_quater_top_(self, mesh):
        """
        Calculates the quarter top position of the given mesh.
        
        :param mesh: Mesh object to calculate position from.
        :rtype: tuple
        :return: Tuple representing the quarter top position (quarter_x, translation_y, center_z)
        """
        bbox = cmds.exactWorldBoundingBox(mesh)
        min_x, min_y, min_z, max_x, max_y, max_z = bbox
        quarter_x = (3 * max_x + min_x) / 4
        center_z = (min_z + max_z) / 2
        translation_y = max_y * 0.8
        return (translation_y, quarter_x, center_z)

    def get_half_positions(self, mesh):
        """
        Calculates the half position (center) of the bounding box of the given mesh.
        
        :param mesh: Mesh object to calculate position from.
        :rtype: tuple
        :return: Tuple representing the center position (half_x, half_y, half_z)
        """
        bbox = cmds.exactWorldBoundingBox(mesh)
        min_x, min_y, min_z, max_x, max_y, max_z = bbox
        half_x = (max_x + min_x) / 2
        half_y = (max_y + min_y) / 2
        half_z = (max_z + min_z) / 2
        return (half_x, half_y, half_z)

    def get_quarter_positions(self, mesh):
        """
        Calculates the quarter position of the bounding box of the given mesh.
        
        :param mesh: Mesh object to calculate position from.
        :rtype: tuple
        :return: Tuple representing the quarter position (quarter_x, quarter_y, quarter_z)
        """
        bbox = cmds.exactWorldBoundingBox(mesh)
        min_x, min_y, min_z, max_x, max_y, max_z = bbox
        quarter_x = (3 * max_x + min_x) / 4
        quarter_y = (3 * max_y + min_y) / 4
        quarter_z = (3 * max_z + min_z) / 4
        return (quarter_x, quarter_y, quarter_z)

    def get_group_center(self, group_name):
        """
        Calculates the center position of all objects within a given group.
        
        :param group_name: Name of the group to calculate position from.
        :rtype: tuple
        :return: Tuple representing the center position (center_x, center_y, center_z) of the group
        """
        children = cmds.listRelatives(group_name, allDescendents=True, type='transform')
        if not children:
            raise ValueError(f"{group_name} group has no children.")
        bbox = cmds.exactWorldBoundingBox(children)
        min_x, min_y, min_z, max_x, max_y, max_z = bbox
        center_x = (min_x + max_x) / 2
        center_y = (min_y + max_y) / 2
        center_z = (min_z + max_z) / 2
        return (center_x, center_y, center_z)

    def get_pos_bottom_minz_center(self, mesh):
        """
        Calculates the bottom minimum Z position of the given mesh.
        
        :param mesh: Mesh object to calculate position from.
        :rtype: tuple
        :return: Tuple representing the bottom minimum Z position (min_y, center_x, min_z)
        """
        bbox = cmds.exactWorldBoundingBox(mesh)
        min_x, min_y, min_z, max_x, max_y, max_z = bbox
        center_x = (min_x + max_x) / 2
        return (min_y, center_x, min_z)

    def get_pos_bottom_maxz_center(self, mesh):
        """
        Calculates the bottom maximum Z position of the given mesh.
        
        :param mesh: Mesh object to calculate position from.
        :rtype: tuple
        :return: Tuple representing the bottom maximum Z position (min_y, center_x, max_z)
        """
        bbox = cmds.exactWorldBoundingBox(mesh)
        min_x, min_y, min_z, max_x, max_y, max_z = bbox
        center_x = (min_x + max_x) / 2
        return (min_y, center_x, max_z)
    
class MeshFinder():
    """
    The MeshFinder class provides utility functions to find meshes based on 
    their name or pattern and also retrieve the top-level group of a given node.
    """

    def find_meshes_with_name(self, name):
        """
        Finds meshes that match the exact name provided.
        
        :param name: Name of the mesh to find.
        :rtype: str or None
        :return: The name of the matching mesh or None if no match is found.
        """
        all_meshes = cmds.ls(type='mesh', long=True)
        for mesh in all_meshes:
            if name == mesh:
                return mesh
        return None

    def find_meshes_with_pattern(self, pattern):
        """
        Finds meshes whose names match the given regular expression pattern.
        
        :param pattern: Regular expression pattern to search for in mesh names.
        :rtype: list or None
        :return: A list of matching mesh names or None if no matches are found.
        """
        all_meshes = cmds.ls(type='mesh', long=True)
        match_meshes = []
        for mesh in all_meshes:
            if re.search(pattern, mesh):
                match_meshes.append(mesh)
        return match_meshes if match_meshes else None

    def get_top_level_group(self, node):
        """
        Recursively finds the top-level group (root group) for the given node.
        
        :param node: Node or mesh for which to find the top-level group.
        :rtype: str
        :return: The name of the top-level group.
        """
        parent = cmds.listRelatives(node, parent=True)
        if not parent:
            return node
        return self.get_top_level_group(parent[0])
