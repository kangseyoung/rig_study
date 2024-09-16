import maya.cmds


objs = cmds.ls(type = "transform")#메쉬와 트랜스폼 노드 모두 포함(grp도 나옴)
def create_hierarchical_joint(obj):
    # obj가 입력되었을 때, 하이어라키 구조를 참고하여,
    # child 메쉬에 해당하는 joint도 만들어준다. 
    # 위치는 어케할지 미정.
    # isrelative 쓸 예정
   
    # 선택 노드 초기화 후에 조인트 생성 이렇게 안하면, 조인트에 자동으로 연결된다.
    obj_joint = cmds.joint(name = f"{obj}_joint") 
    #일단 그룹 별로 joint 생성
    children = cmds.listRelatives(obj, children=True, type="transform") 
    print("children : ",children)
    # 한 그룹의 자식 트랜스폼 노드를 찾아준다.
    if not children:
        return print("there's no childeren")
    # for 문 돌려서 트랜스폼의 자식노드별로 조인트생성 
    for child in children:
        cmds.select(f'{obj_joint}')    
        create_hierarchical_joint(child)
       
        
        
        
for obj in objs:
    if not cmds.listRelatives(obj, parent=True):
        create_hierarchical_joint(obj)