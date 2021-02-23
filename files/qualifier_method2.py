f1=open("teams","r")
f2=open("drop","r")

def get_team_set(f):
    st=set()
    for lines in f:
        st.add(lines.rstrip("\n"))
    return st
st1=get_team_set(f1)
st2=get_team_set(f2)

qualifiers=st1-st2
print(qualifiers)