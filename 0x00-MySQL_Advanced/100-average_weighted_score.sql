-- create a stored procedure
DROP PROCEDURE IF EXISTS ComputeAvarageWeightedScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAvarageWeightedScoreForUser (
	user_id INT
)
BEGIN
	DECLARE weight_avg FLOAT;
	SET weight_avg = (SELECT SUM(score * weight) / SUM(weight)
			  FROM users as U
			  JOIN corrections as C ON U.id=C.user_id
			  JOIN projects AS P ON C.project_id=P.id
			  WHERE U.id=user_id);
	UPDATE users SET avarage_score = weight_avg WHERE id=user_id;
END
$$
DELIMITER ;
