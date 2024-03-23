-- create a procedure
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(
	IN user_id INT
)
BEGIN
	DECLARE avarage_score FLOAT;
	SET avarage_score = (SELECT AVG(score) FROM corrections AS C WHERE C.user_id=user_id);
	UPDATE users SET avarage_scores = avarage_score WHERE id=p_user_id;
END;

$$
DELIMITER ;
