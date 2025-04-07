from app import bot, db, logger, loop, server


if __name__ == "__main__":
    logger.info("Start server connections checking.")

    loop.create_task(server.serve())

    try:
        db.session.connection()
        logger.info("Success connect to database")
    except:
        logger.error("Failed connect to database")
        exit(0)

    bot.start()

    try:
        logger.info("Server started.")
        loop.run_forever()
    except KeyboardInterrupt:
        logger.info("Server prevent stopped.")
    except BaseException as err:
        logger.critical(f"Server prevent stopped. Error: {err}")
