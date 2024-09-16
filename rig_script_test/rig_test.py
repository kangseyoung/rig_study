
import maya.cmds as cmds
# Maya Standalone 환경 해제 (종료할 때)
#메쉬와 트랜스폼 노드 모두 포함(grp도 나옴)

class RigStudyClass():
    """
    마야 리깅 관련 스크립트 공부용 클래스
    """
    def run_create_joint(self):
        except_nodes = ['front', 'persp', 'side', 'top']
        objs = cmds.ls(type = "transform")
        for obj in objs:
            if not obj in except_nodes:
                self.create_hierarchical_joint(obj)

    def create_hierarchical_joint(self,obj):
        """
        obj : mesh
        메쉬를 인풋 값으로 받고,
        메쉬에 위치랑 같은 곳에 
        """
        center_pos = self.get_center_pos(obj)
        
        # 선택 노드 초기화 후에 조인트 생성 이렇게 안하면, 조인트에 자동으로 연결된다.
        obj_joint = cmds.joint(name = f"{obj}_joint", radius= 0.5)
        if not center_pos:
            pos = cmds.xform(obj, query=True, worldSpace=True, translation=True)
            cmds.move(pos[0], pos[1], pos[2], obj_joint)
        else:
            cmds.move(center_pos[0], center_pos[1], center_pos[2], obj_joint)
        #일단 그룹 별로 joint 생성
        children = cmds.listRelatives(obj, children=True, type="transform") 
        print("children : ",children)
        # 한 그룹의 자식 트랜스폼 노드를 찾아준다.
        if not children:
            return print("there's no childeren")
        # for 문 돌려서 트랜스폼의 자식노드별로 조인트생성 
        for child in children:
            cmds.select(f'{obj_joint}')    
            self.create_hierarchical_joint(child)

    def get_center_pos(self,obj):
        shape_node = cmds.listRelatives(obj, shapes=True, fullPath=True)
        if not shape_node:
            return  print("No shape nodes")
        bbox = cmds.exactWorldBoundingBox(shape_node)
        center_pos = [(bbox[0] + bbox[3]) / 2, (bbox[1] + bbox[4]) / 2, (bbox[2] + bbox[5]) / 2]
        return center_pos

joint_maker = RigStudyClass()
joint_maker.run_create_joint()