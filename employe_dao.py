import database
import employe

class employedao:
    connexion=database.connect_db()
    cursor=connexion.cursor()

    def __init__(self) -> None:
        pass



    def create(cls, emp= employe):
      sql= """INSERT INTO employe(nom, prenom, matricule, fonction, departement)
              VALUES(%s,%s,%s,%s,%s)
      """
      params =(employe.nom, employe.prenom, employe.matricule, employe.fonction, employe.departement)
      employedao.cursor.execute(sql, params)
      employedao.connexion.commit()
      employedao.cursor.close()

      return f"L'employe de matricule{emp.matricule}est ajoute avec succes"
    
    def list_all() :
     sql="SELECT * employe"
     employedao.cursor.execute(sql)
     employe= employedao.cursor.fetchall()
     employedao.cursor.close()
     return employe

    def list_one(matricule):
       sql= "SELECT * FROM employe WHERE matricule =%s"
       employedao.cursor.execute(sql,(matricule,))
       employe= employedao.cursor.fetchone()
       employedao.cursor.close()
       return employe

    def delete(matricule):
        sql="DELETE FROM employe WHERE matricule=%s"
        employedao.cursor.execute(sql, (matricule,))
        employedao.connexion.commit()

        return f"L,employe de matricule {emp.matricule} est ajoute avec succes"

    def update(cls, emp=employe):
          sql="""UPDATE employe SET nom=%s, prenom=%s, matricule=%s, fonction=%s, departement=%s
                    WHERE id=1
                    """
          params =(employe.nom, employe.prenom, employe.matricule, employe.fonction, employe.departement)
          employedao.cursor.execute(sql, params)
          employedao.connexion.commit