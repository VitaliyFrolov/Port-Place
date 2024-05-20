import { Container } from '../../Container';
import { Logo } from '../../Logo';
import styles from './Header.module.scss';

export const Header = () => {
    return (
        <div className={styles.header__wrapper}>
            <Container>
                <header className={styles.header}>
                <Logo />
                <nav className={styles.navigation}>
                    <ul className={styles.navigation__list}>
                        <li>
                            О нас
                        </li>
                        <li>
                            Резиденты
                        </li>
                        <li>
                            Игровая зона
                        </li>
                    </ul>
                </nav>
                </header>
            </Container>
        </div>
    );
};