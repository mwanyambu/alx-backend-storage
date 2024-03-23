-- create a stored procedure
DROP PROCEDURE IF EXISTS ComputeAvarageWeightedScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAvarageWeightedScoreForUsers()
BEGIN
	UPDATE users AS U,
		(SELECT SUM(score * weight) / SUM(weight) AS weight_avg
		FROM users as U
		JOIN corrections as C ON U.id=C.user_id
		JOIN projects AS P ON C.project_id=P.id
		GROUP BY U.id)
	AS AW
	SET U.avarage_score = AW.weight_avg
	WHERE U.id=AW.id;
	UPDATE users SET avarage_score = weight_avg WHERE id=user_id;
END
$$
DELIMITER ;
