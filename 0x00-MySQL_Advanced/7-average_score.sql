-- create a procedure
DELIMITER $$

CREATE PROCEDURE ComputeAvarageScoreForUser (
	IN p_user_id INT
)
BEGIN
	DECLARE avarage_score DECIMAL(10, 2);

	SELECT AVG(score) INTO avarage_score
	FROM scores
	WHERE user_id = p_user_id;

	INSERT INTO avarage_scores(user_id, avarage_score)
	VALUES (p_user_id, avarage_score)
	ON DUPLICATE KEY UPDATE avarage_score = avarage_score;
END;

$$
DELIMITER ;
