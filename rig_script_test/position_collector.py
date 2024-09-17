import re
import maya.cmds as cmds

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
        return (center_x, min_y, center_z)

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
        return (quarter_x,translation_y, center_z)

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
        return (center_x, min_y, min_z)

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
        return (center_x, min_y, max_z)