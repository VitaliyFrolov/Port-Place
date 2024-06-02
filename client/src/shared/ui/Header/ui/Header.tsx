'use client'
// import { anchorScroller } from '@/shared/helpers/anchorScroller';
import { useScrollTrigger } from '@/shared/hooks/useScrollTrigger';
import { Container } from '../../Container';
import { Logo } from '../../Logo';
import styles from './Header.module.scss';

export const Header = () => {
    const scrolled = useScrollTrigger();

    // useEffect(() => {
    //     if (scrolled === true) {
    //         anchorScroller('page');
    //     }
    // }, [scrolled]);

    return (
        <header
            className={styles.header__wrapper}
            style={scrolled ? { opacity: "1" } : { opacity: "0" }}
        >
            <Container>
                <div className={styles.header}>
                    <Logo />
                    <nav className={styles.navigation}>
                        <ul className={styles.navigation__list}>
                            <li className={styles.navigation__item}>
                                Главная
                            </li>
                            <li className={styles.navigation__item}>
                                Блог
                            </li>
                            <li className={styles.navigation__item}>
                                Игровая зона
                            </li>
                        </ul>
                    </nav>
                </div>
            </Container>
        </header>
    );
};